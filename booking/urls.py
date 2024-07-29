from django.urls import path
from . import views

urlpatterns = [
    path("", views.home1),
    path("signup", views.signup),
    path("login", views.signin),
    path("signout", views.signout),
    path("home", views.home),
    path("search", views.search, name="search"),
    path("addinfo/<int:id>", views.add_info, name="addinfo"),
    path(
        "addinfo/<int:id>/<int:passenger_id>/<int:seats>/displayinfo",
        views.display_info,
        name="displayinfo",
    ),
    path(
        "addinfo/<int:id>/<int:passenger_id>/<int:seats>/cardinfo",
        views.card_info,
        name="cardinfo",
    ),
    path(
        "addinfo/<int:id>/<int:passenger_id>/<int:seats>/final",
        views.finalpage,
        name="final",
    ),
    path("match/", views.find_state, name="find"),
    path("redirect-to-port-8001/", views.redirect_to_port_8001, name='redirect_to_port_8001'),
    path('feedback/', views.submit_feedback, name='submit_feedback'),
    path('thank-you/', views.thank_you, name='thank_you'),
]



