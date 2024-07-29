from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from booking.models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import *
from django.forms import modelformset_factory
from datetime import datetime
from .emails import send_email
from .weather import city
from .cap import cap
from .word import generate_random_word
from .image import get_image_link
from .card_valid import valid




# Create your views here.
def home1(request):
    return render(request, "home2.html")



def find_state(request):
    query = request.GET.get("state_name")
    matching_title = None
    states_auto = Ebrochure2.objects.all()
    context = {"states_auto": states_auto}
    if query:
        matching_title = Ebrochure2.objects.filter(state__icontains=query).first()
        state = matching_title.state.upper()

        resp = city(query)
        temp, feels, humid, desc, wind, timenow = (
            resp[0],
            resp[1],
            resp[2],
            resp[3],
            resp[4],
            datetime.now,
        )
        image = get_image_link(desc)
        context = {
            "state": state,
            "matching_title": matching_title,
            "temp": temp,
            "feels": feels,
            "humid": humid,
            "desc": desc,
            "wind": wind,
            "time": timenow,
            "image": image,
        }

    return render(request, "find_state.html", context)


def home(request):
    return render(request, "home.html")

def signup(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        pwd = request.POST.get("password")
        pwd2 = request.POST.get("confirm-password")
        cap_user = request.POST.get("cap")

        
        cap_data = request.session.get("cap_data")

        print(cap_user, " == ", cap_data)  

        if len(pwd) > 8:
            if pwd == pwd2:
                if cap_data == cap_user:
                    if not User.objects.filter(username=name).exists():
                        if not User.objects.filter(email=email).exists():
                            u = User.objects.create_user(
                                username=name, email=email, password=pwd
                            )
                            u.save()
                            send_email(email)
                            messages.success(
                                request, "Login now. Check mail. Surprise!"
                            )
                            return redirect("/login")
                        else:
                            messages.error(request, "Email already exists.")
                    else:
                        messages.error(request, "Username already exists.")
                else:
                    messages.error(request, "Wrong captcha.")
            else:
                messages.error(request, "Passwords do not match.")
        else:
            messages.error(request, "Password must be at least 8 characters long.")

    # Generate a new captcha value and store it in the session
    cap_data = generate_random_word()
    request.session["cap_data"] = cap_data
    cap(cap_data)

    return render(request, "signup.html")


def signin(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f"Welcome, {username}!")
                return redirect("/home")  # Redirect to your home page
        else:
            messages.error(request, "Invalid username or password.")
            return render(request, "login.html", {"form": form})
    else:
        form = AuthenticationForm()
        return render(request, "login.html", {"form": form})


def signout(request):
    logout(request)
    messages.success(request, "Logged Out Successfully!!")
    return redirect("/login")


def search(request):
    stations_autocomplete = Stations.objects.all()
    context = {"stations": stations_autocomplete}
    if request.method == "POST":
        dep_station = request.POST["dep_station"]
        arv_station = request.POST["arv_station"]
        trains = Trains.objects.filter(dep_station=dep_station, arv_station=arv_station)

        context = {
            "trains": trains,
        }

    return render(request, "search.html", context)


def add_info(request, id):
    context = {}
    seats = int(request.GET["seats"])
    a = Trains.objects.get(id=id)
    if seats > int(a.seats_avl):
        messages.error(
            request,
            f"{seats} seats not available! Number of seats available is {a.seats_avl}.",
        )
        return redirect("search")
    if seats < 1:
        messages.error(
            request, "Invalid Input.Number of Seats should be positive. Are you dumb?"
        )
        return redirect("search")
    u = Passenger()
    u.from_location = a.dep_station
    u.to_location = a.arv_station
    a_train_instance = Trains.objects.get(train_name=a.train_name)
    u.train_name = a_train_instance
    u.save()
    pformset = modelformset_factory(
        PassengerInfo, fields=["name", "age", "gender", "berth"], extra=seats
    )
    if request.method == "POST":
        passenger_formset = pformset(
            request.POST, queryset=PassengerInfo.objects.none()
        )
        if passenger_formset.is_valid():
            instances = passenger_formset.save(commit=False)
            for instance in instances:
                instance.trip_id = u
                instance.save()
            passenger_formset.save_m2m()
            return redirect("displayinfo", id=id, passenger_id=u.trip_id, seats=seats)
    else:
        passenger_formset = pformset(queryset=PassengerInfo.objects.none())
    context = {"a": a, "formset": passenger_formset}
    return render(request, "addinfo.html", context)


def display_info(request, id, passenger_id, seats):
    a = Trains.objects.get(id=id)
    passenger = PassengerInfo.objects.filter(trip_id=passenger_id)
    context = {"a": a, "details": passenger}
    if request.method == "get":
        return redirect("cardinfo", id=id, passenger_id=passenger_id, seats=seats)
    return render(request, "display_info.html", context)


def card_info(request, id, passenger_id, seats):
    if request.method == "POST":
        card_number = request.POST["cardNumber"]
        resp = valid(card_number)
        if resp:
            print("Card okay")
            return redirect("final", id=id, passenger_id=passenger_id, seats=seats)
        else:
            print("Card not okay")
            messages.error(request, "Wrong Card Number!!")
    return render(request, "card.html")


def finalpage(request, id, passenger_id, seats):
    a = Trains.objects.get(id=id)
    a.seats_avl = int(a.seats_avl) - seats
    a.save()
    passenger = PassengerInfo.objects.filter(trip_id=passenger_id)
    date_time = datetime.now
    context = {"a": a, "details": passenger, "date": date_time}
    return render(request, "ticketfinal.html", context)

def redirect_to_port_8001(request):
    # Redirect to port 8001
    return redirect('http://localhost:8001/')


def submit_feedback(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        rating = request.POST.get('rating')
        review = request.POST.get('review')
        Feedback.objects.create(fd_name=name, fd_email=email, fd_rating=rating, fd_review=review)
        return redirect('thank_you')  # Redirect after submission
    return render(request, 'feedback_form.html')

def thank_you(request):
    return render(request, 'thank_you.html')

