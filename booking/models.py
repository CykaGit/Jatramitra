from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Ebrochure2(models.Model):
    state = models.CharField(max_length=25, unique=True, default='',null=True,blank=True)
    state_capital = models.CharField(max_length=25, default='Capital : ',null=True,blank=True)
    gnrl_desc = models.TextField(default='',null=True,blank=True)
    places_to_visit = models.TextField(default='',null=True,blank=True)
    time_to_visit = models.TextField(default='',null=True,blank=True)
    climate = models.TextField(default='',null=True,blank=True)
    culture = models.TextField(default='',null=True,blank=True)
    famous_foods = models.TextField(default='',null=True,blank=True)
    imgs = models.ImageField(null=True, upload_to="images/")

    def __str__(self):
        return self.state


class Stations(models.Model):
    station_name=models.CharField(max_length=50, primary_key=True)
    station_code=models.CharField(max_length=10)
    station_location=models.CharField(max_length=30)
    class Meta:
        db_table='Stations'
    def __str__(self):
        return self.station_name



class Trains(models.Model):
    train_name=models.CharField(max_length=50)
    train_number=models.IntegerField()
    dep_station = models.ForeignKey(Stations, related_name="departures", on_delete=models.CASCADE ,default='')
    arv_station = models.ForeignKey(Stations, related_name="arrivals", on_delete=models.CASCADE ,default='')
    dep_time=models.TimeField()
    arv_time=models.TimeField()
    run_days=models.CharField(max_length=50)
    seats_avl=models.CharField(max_length=100)
    seat_quotas=models.CharField(max_length=100)
    seat_classes=models.CharField(max_length=50)
    
    def __str__(self):
        return f"{self.train_name} from {self.dep_station} to {self.arv_station}"
    class Meta:
        db_table='Trains'

class Passenger(models.Model):
    trip_id=models.AutoField(primary_key=True,verbose_name="id")
    from_location=models.ForeignKey(Stations,on_delete=models.CASCADE,related_name='departure')
    to_location=models.ForeignKey(Stations,on_delete=models.CASCADE,related_name='arrival')
    train_name=models.ForeignKey(Trains,on_delete=models.CASCADE,related_name='trainname',default='')
    class Meta:
        db_table='Passenger'


class PassengerInfo(models.Model):
    name=models.CharField(max_length=120)
    age=models.IntegerField()
    gender = models.CharField(max_length=10, choices=[('Male', 'Male'), ('Female', 'Female'), ('Others', 'Others')])
    berth = models.CharField(max_length=10, choices=[('1AC', '1AC'), ('2AC', '2AC'), ('3AC', '3AC'), ('2AS', '2AS')])
    trip_id=models.ForeignKey(Passenger,on_delete=models.CASCADE)
    class Meta:
        db_table='PassengerInfo'
    def __str__(self):
        return self.name




class Feedback(models.Model):
    fd_name = models.CharField(blank=True,null=True ,max_length=100)
    fd_email = models.EmailField(blank=True,null=True)
    fd_rating = models.IntegerField(blank=True,null=True)
    fd_review = models.TextField(blank=True,null=True, max_length=150)
    fd_created_at = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return f"{self.fd_name} - {self.fd_rating}"