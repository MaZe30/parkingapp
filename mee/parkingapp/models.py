from django.db import models
from django.db import connections
from django import forms
from django.db.models.base import Model
from django.db.models.fields import CharField, IntegerField


class Newuser(models.Model):
    Username=models.CharField(max_length=150)
    Email=models.CharField(max_length=150)
    Pwd=models.CharField(max_length=150)
    Age=models.IntegerField()
    class Meta:
        db_table="parkingapp_newuser"



class Parkingmjesto(models.Model):
    ParkingMjesto=models.CharField(max_length=150)
    Username=models.CharField(max_length=25)
    Registracija=models.CharField(max_length=100)
    Datum=models.CharField(max_length=50)
    Vrijeme=models.CharField(max_length=50)
    Satnica=models.IntegerField()
    KM=models.IntegerField()
class PlacanjeSms(models.Model):
    BrojTelefona=models.CharField(max_length=50)
    
    Username=models.CharField(max_length=50)
    Datum=models.CharField(max_length=50)
    Vrijeme=models.CharField(max_length=50)
    
class PlacanjeKarticno(models.Model):
    Ime=models.CharField(max_length=100)
    
    BrojKartice=models.CharField(max_length=20)
    Username=models.CharField(max_length=20)
    Datum=models.CharField(max_length=50)
    Vrijeme=models.CharField(max_length=50)
class Rezervacija(models.Model):
    Username=models.CharField(max_length=50)
    Datum=models.CharField(max_length=20)
    Satnica=models.CharField(max_length=30)
    Kod=IntegerField()
    
class Parking(models.Model):
    NazivMjesta=models.CharField(max_length=20)
    BrojMjesta=models.IntegerField()
    class Meta:
        db_table="parkingapp_parking"

class Parking2(models.Model):
    NazivMjesta=models.CharField(max_length=20)
    BrojMjesta=models.IntegerField()
    class Meta:
        db_table="parkingapp_parking2"