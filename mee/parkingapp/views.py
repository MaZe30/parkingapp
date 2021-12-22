from typing import NoReturn
from django.db.models.query import EmptyQuerySet
from django.http import request
from django.http.response import HttpResponseRedirect
import mysql.connector
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",
    database="parking"
    

)




mycursor=mydb.cursor()
from django.shortcuts import redirect, render
from parkingapp.models import Newuser
from django.contrib import messages
from parkingapp.models import Parkingmjesto
from parkingapp.models import PlacanjeSms
from parkingapp.models import PlacanjeKarticno
from parkingapp.models import Rezervacija
from datetime import date,datetime
from parkingapp.models import Parking,Parking2
import time
today=date.today()
now = datetime.now()






  
import random

def Indexpage(request):
    return render(request,'pocetna.html')

def Userrreg(request):
    if request.method=='POST':
        Username=request.POST['Username']
        Email=request.POST['Email']
        Pwd=request.POST['Pwd']
        Age=int(request.POST['Age'])
        if Age < 18:
            messages.success(request,"Korisnicima ispod 18 godina nije dozvoljeno placanje")
            return render(request,'registracija.html')
        else:
            Newuser(Username=Username,Email=Email,Pwd=Pwd,Age=Age).save()
            messages.success(request,'Novi korisnik '+request.POST['Username']+" je uspiješno spašen")
            return render(request,'registracija.html')
    else:
        return render(request,'registracija.html')
            

    


    
def back(request):
    return render(request,'pocetna.html')


from django.db.models import Sum

def logincheck(request):
    if request.method=='POST':    
        username=request.POST['Email1']
        sifra=request.POST['Pwd1']
        sql="SELECT * FROM parkingapp_newuser WHERE Email=%s AND Pwd=%s"
        val=(username,sifra)
        mycursor.execute(sql,val)
        res=mycursor.fetchone()
        request.session['user']=username
        
        
        
        if username=='admin1@gmail.com' and sifra=='admin':
            return render(request,'admin.html')
            
    
        if not res:
            messages.success(request,'Pogrešna šifra ili username')
            return render(request,'pocetna.html')
        else:
            
                                           

            return render(request,'userpocetna.html',{"username" : username })
    else:
        return render (request,'pocetna.html')

def parkiraj(request):
    
    return render(request,'zone.html',{"username": request.session['user']})
    


        
        
            
    

from django.db.models import F

def parkingspot(request):
    if request.method=="POST":
        
        
        parking=request.POST['zona1']
        Registracija=request.POST['tablica']
        Username=request.session['user']
        Satnica=request.POST['Satnica']
        Datum = today.strftime("%m/%d/%y")
        Vrijeme=now.strftime("%H:%M:%S")
       

        
        
        
        Parking.objects.filter(NazivMjesta=parking).update(BrojMjesta=F('BrojMjesta') - 1)
        
        
        
        
        Parkingmjesto(ParkingMjesto=parking,Registracija=Registracija,Username=Username,Datum=Datum,Vrijeme=Vrijeme,Satnica=Satnica,KM=(int(Satnica) + int(Satnica))).save()
            
        return render(request,'birajplacanje.html',{"username":Username})
        
            
            
        
            
        
            

def parkingspot1(request):
    if request.method=="POST":
        parking=request.POST['zona2'] 
        Registracija=request.POST['tablica']
        Username=request.session['user']
        Datum = today.strftime("%m/%d/%y")
        Vrijeme=now.strftime("%H:%M:%S")
        Satnica=request.POST['Satnica']
        

        
        Parking2.objects.filter(NazivMjesta=parking).update(BrojMjesta=F('BrojMjesta') - 1)
        
        
        
        
        Parkingmjesto(ParkingMjesto=parking,Registracija=Registracija,Username=Username,Datum=Datum,Vrijeme=Vrijeme,Satnica=Satnica,KM=(int(Satnica) + int(Satnica))).save()
            
        return render(request,'birajplacanje.html',{"username":Username})
    
def sms(request):
    
        if request.method=='POST':
            BrojTelefona=request.POST['BrojTelefona']
            
            Username=request.session['user']
            Datum = today.strftime("%m/%d/%y")
            Vrijeme=now.strftime("%H:%M:%S")
            PlacanjeSms(BrojTelefona=BrojTelefona,Username=Username,Datum=Datum,Vrijeme=Vrijeme).save()
            messages.success(request,'Uspiješno ste uplatili parking')
            return render(request,'placanje1.html',{"username":Username})

def kartica(request):
    
        if request.method=='POST':
            Ime=request.POST['Ime']
            
            BrojKartice=request.POST['BrojKartice']
            Username=request.session['user']
            Datum = today.strftime("%m/%d/%y")
            Vrijeme=now.strftime("%H:%M:%S")
    

            PlacanjeKarticno(Ime=Ime,BrojKartice=BrojKartice,Username=Username,Datum=Datum,Vrijeme=Vrijeme).save()
            messages.success(request,'Uspiješno ste uplatili ' + request.POST ['Satnica'] +' sati/a parkinga')
            return render(request,'placanje2.html',{"username":Username})
    
from parkingapp.models import Parking,Parking2   
def zona1(request):
    lista=Parking.objects.all()
    return render(request,'parkingmjesto1.html',{"lista":lista,"username": request.session['user']})

def zona2(request):
    lista=Parking2.objects.all
    return render(request,'parkingmjesto2.html',{"lista":lista,"username": request.session['user']})

def placanje1(request):
    return render(request,'placanje1.html',{"username": request.session['user']})

def placanje2(request):
    return render(request,'placanje2.html',{"username": request.session['user']})

def listausera(request):
    
    return render(request,'listausera.html')

def show(request):
    result=Newuser.objects.all()
    return render(request,'listausera.html',{'Newuser': result})


def listaparkinga(request):
    lista=Parking.objects.all()
    lista1=Parking2.objects.all()
    sumres=Parkingmjesto.objects.all().aggregate(Sum('KM'))
            
    
    
    return render(request,'listaparkinga.html',{"lista":lista,"lista1":lista1,"ukupno":sumres["KM__sum"]})


def delete(request):
    if request.method=="POST":
        value=request.POST['Email12']
        instance = Newuser.objects.get(Email=value)
        instance.delete()
        result=Newuser.objects.all()
       
        messages.success(request,"Uspiješno ste obrisali korisnika")
    return render(request,"listausera1.html",{"Newuser":result})
 
    


def rezervisi(request):
    Username=request.session['user']
    return render(request,'rezervacija.html',{"username":Username})
def userpregled(request):
    return render(request,'pregleduser.html')


def rezervacija(request):
    if request.method=='POST':
        Username=request.session['user']
        Datum = request.POST['Datum']
        Satnica=request.POST['Satnica']
        Kod=random.randint(1000,9999)
        request.session['Kod']=Kod
        Rezervacija(Username=Username,Satnica=Satnica,Datum=Datum,Kod=Kod).save()
        messages.success(request,'Uspijesno ste rezervisali parking,Vas kod je:' + str(Kod))
        return render(request,'rezervacija.html',{'KOD ': request.session['Kod'] ,"username":Username})

    
def pregledaj(request):
    Username=request.session['user']
    return render(request,'pregleduserparkinga.html',{"username":Username})
    
def show1(request):
    username=request.session['user']
    result=Parkingmjesto.objects.all().filter(Username=username)
    result1=PlacanjeSms.objects.all().filter(Username=username)
    result2=PlacanjeKarticno.objects.all().filter(Username=username)
    result3=Rezervacija.objects.all().filter(Username=username)
    sumres=Parkingmjesto.objects.filter(Username=username).aggregate(Sum('KM'))
    return render(request,'pregleduserparkinga.html',{"sumres":sumres['KM__sum'],'Parkingmjesto': result,"Parkingmjesto1":result1,"Parkingmjesto2":result2,"username":username,"rezervacija":result3})
    
def pocetna(request):
    return render(request,"userpocetna.html",{"username":request.session['user']})
def odjava(request):
    return render(request,"pocetna.html")
def pocetna1(request):
    username=request.session['user']
    return render(request,"admin.html",{"username":username})
def rezervacijaadmin(request):
    return render(request,"rezervacijaadmin.html")
def kod(request):
    username=request.session['user']
    return render(request,"rezervacijakod.html",{"username":username})

def kod1(request):
    if request.method=="POST":
        username=request.session['user']
        kod=request.POST['kod']
        
        
        res=Rezervacija.objects.all().filter(Kod=kod)

        if not res:
            messages.success(request,"Vaš kod je istekao ili je nepostojeći,pokušajte ponovo!")
            return render(request,"rezervacijakod.html",{"username":username})
            
        else:
            return render(request,"zone.html",{"username":username})
            
def brojmjesta(request):
    username=request.session['user']
    lista=Parking.objects.all()
    
    
    return render(request,'brojmjesta.html',{"lista":lista,"username":username})
def datum(request):
    return render(request,"pregledpodatumu.html")

def datum2(request):
    if request.method=='POST': 
        datum=request.POST['datum']   
        
        result=Parkingmjesto.objects.all().filter(Datum=datum)
        if (len(result) == 0):
        
            messages.success(request,"Nema rezultata,provjerite da li je unos u traženom formatu!")
            return render(request,"pregleddatum.html",{"datum":result})
        else:
            messages.success(request,"Nema rezultata,provjerite da li je unatu!")
            return render(request,"pregleddatum.html",{"datum":result})
         

def manage(request):
    return render(request,'manageparking.html')
def dodaj1(request):
    return render(request,'dodaj.html')



def dodaj(request):
    if request.method=="POST":
        if request.POST['zona'] == "zona1":
            lista=Parking.objects.all()
            lista1=Parking2.objects.all()
            sql="insert into parkingapp_parking (NazivMjesta,BrojMjesta) values (%s,%s)"
            val=(request.POST['naziv'],request.POST['broj'])
            mycursor.execute(sql,val)
            mydb.commit()
            messages.success(request,"Uspiješno ste dodali parking mjesto!")
            
            return render(request,'listaparkinga.html',{"lista":lista,"lista1":lista1})
        if request.POST['zona'] == "zona2":
            lista=Parking.objects.all()
            lista1=Parking2.objects.all()
            sql="insert into parkingapp_parking2 (NazivMjesta,BrojMjesta) values (%s,%s)"
            val=(request.POST['naziv'],request.POST['broj'])
            mycursor.execute(sql,val)
            mydb.commit()
            return render(request,'listaparkinga.html',{"lista":lista,"lista1":lista1})
        

def obrisi1(request):
    lista=Parking.objects.all()
    lista1=Parking2.objects.all()
    return render(request,'obrisi.html',{"lista":lista,"lista1":lista1})
   

def obrisi(request):
    if request.method=="POST":
        if request.POST['zona'] == "zona1":
            instance = Parking.objects.get(NazivMjesta=request.POST['naziv'])
            instance.delete()
            lista=Parking.objects.all()
            lista1=Parking2.objects.all()
            return render(request,'listaparkinga.html',{"lista":lista,"lista1":lista1})
        if request.POST['zona'] == "zona2":
            instance = Parking2.objects.get(NazivMjesta=request.POST['naziv'])
            instance.delete()
            lista=Parking.objects.all()
            lista1=Parking2.objects.all()
            return render(request,'listaparkinga.html',{"lista":lista,"lista1":lista1})

def uredi1(request):
    lista=Parking.objects.all()
    lista1=Parking2.objects.all()
    return render(request,'uredi.html',{"lista":lista,"lista1":lista1})

def uredi(request):
    if request.method=="POST":
        if request.POST['zona']=="zona1":
            Parking.objects.filter(NazivMjesta=request.POST['naziv']).update(NazivMjesta=request.POST['naziv1'],BrojMjesta=request.POST['broj'])
            lista=Parking.objects.all()
            lista1=Parking2.objects.all()
            return render(request,'listaparkinga.html',{"lista":lista,"lista1":lista1})
        if request.POST['zona']=="zona2":
            Parking2.objects.filter(NazivMjesta=request.POST['naziv']).update(NazivMjesta=request.POST['naziv1'],BrojMjesta=request.POST['broj'])
            lista=Parking.objects.all()
            lista1=Parking2.objects.all()
            return render(request,'listaparkinga.html',{"lista":lista,"lista1":lista1})
    
        


