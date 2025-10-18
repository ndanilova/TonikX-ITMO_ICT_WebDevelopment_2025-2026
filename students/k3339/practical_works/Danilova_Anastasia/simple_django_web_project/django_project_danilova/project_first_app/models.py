from django.db import models


class CarOwner(models.Model):
    last_name = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30)
    date_of_birth = models.DateField(null=True)


class Car(models.Model):
    license_plate = models.CharField(max_length=15)
    brand = models.CharField(max_length=20)
    model = models.CharField(max_length=20)
    color = models.CharField(max_length=30, null=True, blank=True)


class Ownership(models.Model):
    car_owner = models.ForeignKey(CarOwner, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    date_started = models.DateField()
    date_ended = models.DateField(null=True, blank=True)


class DriversLicense(models.Model):
    car_owner = models.ForeignKey(CarOwner, on_delete=models.CASCADE)
    license_number = models.CharField(max_length=10)
    license_type = models.CharField(max_length=10)
    date_of_issue = models.DateField()
