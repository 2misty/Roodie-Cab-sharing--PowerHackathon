from django.db import models
# sharing/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    is_car_owner = models.BooleanField(default=False)
# sharing/models.py


class User(AbstractUser):
    is_car_owner = models.BooleanField(default=False)

class RideRequest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    start_location = models.CharField(max_length=255)
    destination = models.CharField(max_length=255)
    ride_time = models.DateTimeField()
    is_accepted = models.BooleanField(default=False)
    accepted_by = models.ForeignKey(User, related_name='accepted_rides', null=True, blank=True, on_delete=models.SET_NULL)

