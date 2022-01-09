import re
from typing import NoReturn
from django.db.models.query import EmptyQuerySet
from django.http import request
from django.http.response import HttpResponseRedirect
import mysql.connector
from django.http import HttpResponse
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",
    database="parking"
    

)




mycursor=mydb.cursor()

from django.shortcuts import redirect, render
from parkingapp.models import AdminPanel, Newuser
from django.contrib import messages
from parkingapp.models import Parkingmjesto
from parkingapp.models import PlacanjeSms
from parkingapp.models import PlacanjeKarticno
from parkingapp.models import Rezervacija
from datetime import date,datetime,timedelta
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
        res=Newuser.objects.filter(Email=Email).count()
        if Age < 18:
            messages.success(request,"Korisnicima ispod 18 godina nije dozvoljeno placanje")
            return render(request,'registracija.html')
        if res > 0:
            messages.success(request,"Email koji ste unijeli je već registrovan,pokušajte drugi !")
            return render(request,"registracija.html")
            
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
        res=Newuser.objects.filter(Email=username,Pwd=sifra).count()
        request.session['user']=username
        
        
        
        if username=='admin1@gmail.com' and sifra=='admin':
            return render(request,'admin.html')
            
    
        if res==0:
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
        VrijemePrijave=now.strftime("%H:%M:%S")
        VrijemeOdjave=(datetime.now() + timedelta(hours=int(Satnica))).strftime('%H:%M:%S')
        Kod=0000
        if parking =="zona1":
            messages.success(request,"Molimo odaberite parkingmjesto")
            return render(request,"parkingmjesto1.html",{"username":Username})
        

        
        
        
       
        
        
        
        
        Parkingmjesto(ParkingMjesto=parking,Kod=Kod,Registracija=Registracija,Username=Username,Datum=Datum,VrijemePrijave=VrijemePrijave,VrijemeOdjave=VrijemeOdjave,Satnica=Satnica,KM=(int(Satnica) + int(Satnica))).save()
        sql="select * from parkingapp_parkingmjesto "
    
        mycursor.execute(sql)
        rows = mycursor.fetchall() 
        
        
        
            
        return render(request,'birajplacanje.html',{"username":Username})
        
            
            


            
        
            

def parkingspot1(request):
    
        
    if request.method=="POST":
        
        parking=request.POST['zona2'] 
        Registracija=request.POST['tablica']
        Username=request.session['user']
        Datum = today.strftime("%m/%d/%y")
        Satnica=request.POST['Satnica']
        VrijemePrijave=now.strftime("%H:%M:%S")
        VrijemeOdjave=(datetime.now() + timedelta(hours=int(Satnica))).strftime('%H:%M:%S')
        Kod=0000
    
        
        

        
        
        
        
        
        
        Parkingmjesto(ParkingMjesto=parking,Kod=Kod,Registracija=Registracija,Username=Username,Datum=Datum,VrijemePrijave=VrijemePrijave,VrijemeOdjave=VrijemeOdjave,Satnica=Satnica,KM=(int(Satnica) + int(Satnica))).save()
        

          
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
            messages.success(request,'Uspiješno ste uplatili parking')
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

cursor = mydb.cursor(dictionary=True)


def listaparkinga(request):
    Datum = today.strftime("%m/%d/%y")
    Vrijeme=now.strftime("%H:%M:%S")
    lista=Parking.objects.all()
    lista1=Parking2.objects.all()
    sumres=Parkingmjesto.objects.all().aggregate(Sum('KM'))
    
    
    
    sql="select NazivMjesta from parkingapp_parking  "
    
    mycursor.execute(sql)
    nazivparkinga = mycursor.fetchall()
    
    sql="select NazivMjesta from parkingapp_parking2   "
    
    mycursor.execute(sql)
    nazivparkinga2 = mycursor.fetchall()


    
    sumaparking1=[]
    r=0
    
    
    
        
    sql="Select BrojMjesta from parkingapp_parking"
    mycursor.execute(sql)
    pp=mycursor.fetchall()
    
    
    b1=[]
    bb1=[]
    for ss in nazivparkinga:
        counter=0
        counter=Parkingmjesto.objects.filter(ParkingMjesto=ss[0],Datum=Datum,VrijemeOdjave__gte=Vrijeme).count()
        bb1.append(counter)
    c1=[]
    broj1=0
    for xs in pp:
        number=0
        number=xs[0]-bb1[broj1]
        b1.append(number)
        broj1=broj1 + 1
    

    sql="Select BrojMjesta from parkingapp_parking2"
    mycursor.execute(sql)
    pp1=mycursor.fetchall()
    ii=0

    cc1=[]
    

    for s in nazivparkinga2:
        counter=0
        counter=Parkingmjesto.objects.filter(ParkingMjesto=s[0],Datum=Datum,VrijemeOdjave__gte=Vrijeme).count()
        cc1.append(counter)
    c1=[]
    broj=0
    for xx in pp1:
        number=0
        number=xx[0]-cc1[broj]
        c1.append(number)
        broj=broj + 1



    
    
    
    
    

        
            




    return render(request,'listaparkinga.html',{"lista":lista,"lista1":lista1,"ukupno":sumres["KM__sum"],"suma":b1,"suma1":c1})
        
  

        


    
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
    lista=Parking.objects.all()
    lista1=Parking2.objects.all()
    return render(request,'rezervacija.html',{"username":Username,"lista":lista,"lista1":lista1})
def userpregled(request):
    return render(request,'pregleduser.html')


def rezervacija(request):
    if request.method=='POST':
        Username=request.session['user']
        ParkingMjesto=request.POST['parking']
        Datum = request.POST['Datum']
        Satnica=request.POST['Satnica']
        VrijemePrijave=now.strftime("%H:%M:%S")
        VrijemeOdjave=(datetime.now() + timedelta(hours=int(Satnica))).strftime('%H:%M:%S')
        Kod=random.randint(1000,9999)
        Registracija=request.POST['registracija']
        request.session['Kod']=Kod
        format = "%m/%d/%y"
        lista=Parking.objects.all()
        lista1=Parking2.objects.all()




        try:
            datetime.strptime(Datum, format)
            Rezervacija(ParkingMjesto=Parkingmjesto,Username=Username,Satnica=Satnica,Datum=Datum,VrijemePrijave=VrijemePrijave,VrijemeOdjave=VrijemeOdjave,Kod=Kod).save()
            Parkingmjesto(ParkingMjesto=ParkingMjesto,Registracija=Registracija,Username=Username,Satnica=Satnica,Datum=Datum,Kod=Kod,VrijemePrijave=VrijemePrijave,VrijemeOdjave=VrijemeOdjave,KM=(int(Satnica) + int(Satnica))).save()
            messages.success(request,'Uspiješno ste rezervisali parking,Vaš kod je:' + str(Kod))
            return render(request,'rezervacija.html',{'KOD ': request.session['Kod'] ,"username":Username,"lista":lista,"lista1":lista1})
        
        except ValueError:
            messages.success(request,"Došlo je do greške,provjerite format datuma!")

            lista=Parking.objects.all()
            lista1=Parking2.objects.all()
            return render(request,'rezervacija.html',{"username":Username,"lista":lista,"lista1":lista1})
        
       

    
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
    lista=Parking.objects.all()
    lista1=Parking2.objects.all()
    return render(request,'rezervacijaadmin.html',{"lista":lista,"lista1":lista1})
def rezervacija12(request):
    if request.method=='POST':
        Username="admin"
        ParkingMjesto=request.POST['parking']
        Datum = request.POST['Datum']
        Satnica=request.POST['Satnica']
        VrijemePrijave=now.strftime("%H:%M:%S")
        VrijemeOdjave=(datetime.now() + timedelta(hours=int(Satnica))).strftime('%H:%M:%S')
        Kod=random.randint(1000,9999)
        format = "%m/%d/%y"
        request.session['Kod']=Kod
        lista=Parking.objects.all()
        lista1=Parking2.objects.all()




        try:
            datetime.strptime(Datum, format)
            Rezervacija(ParkingMjesto=Parkingmjesto,Username=Username,Satnica=Satnica,Datum=Datum,VrijemePrijave=VrijemePrijave,VrijemeOdjave=VrijemeOdjave,Kod=Kod).save()
            Parkingmjesto(ParkingMjesto=ParkingMjesto,Username=Username,Satnica=Satnica,Datum=Datum,VrijemePrijave=VrijemePrijave,Kod=Kod,VrijemeOdjave=VrijemeOdjave,KM=(int(Satnica) + int(Satnica))).save()
            messages.success(request,'Uspiješno ste rezervisali parking,Vaš kod je:' + str(Kod))
            return render(request,'rezervacijaadmin.html',{'KOD ': request.session['Kod'] ,"lista":lista,"lista1":lista1})
        
        except ValueError:
            messages.success(request,"Došlo je do greške,provjerite format datuma!")

            lista=Parking.objects.all()
            lista1=Parking2.objects.all()
            return render(request,'rezervacijaadmin.html',{"lista":lista,"lista1":lista1})
        

    
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
            return render(request,"birajplacanje.html",{"username":username})

Datum = today.strftime("%m/%d/%y")
    
Vrijeme=now.strftime("%H:%M:%S")



def brojmjesta(request):
    
    
    
    username=request.session['user']
    Datum = today.strftime("%m/%d/%y")
    
    Vrijeme=now.strftime("%H:%M:%S")
    lista=Parking.objects.all()
    lista1=Parking2.objects.all()
    test=Parkingmjesto.objects.all()
    sql="select NazivMjesta from parkingapp_parking"
    
    mycursor.execute(sql)
    nazivparkinga = mycursor.fetchall()
        
    sql="select NazivMjesta from parkingapp_parking2"
        
    mycursor.execute(sql)
    nazivparkinga2 = mycursor.fetchall()
    


    
    sumaparking1=[]
    
    
        

   
        
        
            
    sql="Select BrojMjesta from parkingapp_parking"
    mycursor.execute(sql)
    pp=mycursor.fetchall()
    i=0
    b1=[]
    bb1=[]
    for ss in nazivparkinga:
        counter=0
        counter=Parkingmjesto.objects.filter(ParkingMjesto=ss[0],Datum=Datum,VrijemeOdjave__gte=Vrijeme).count()
        bb1.append(counter)
    c1=[]
    broj1=0
    for xs in pp:
        number=0
        number=xs[0]-bb1[broj1]
        b1.append(number)
        broj1=broj1 + 1
    

    sql="Select BrojMjesta from parkingapp_parking2"
    mycursor.execute(sql)
    pp1=mycursor.fetchall()
    ii=0

    cc1=[]
    

    for s in nazivparkinga2:
        counter=0
        counter=Parkingmjesto.objects.filter(ParkingMjesto=s[0],Datum=Datum,VrijemeOdjave__gte=Vrijeme).count()
        cc1.append(counter)
    c1=[]
    broj=0
    for xx in pp1:
        number=0
        number=xx[0]-cc1[broj]
        c1.append(number)
        broj=broj + 1
    

    
    
    return render(request,'brojmjesta.html',{"lista":lista,"username":username,"lista1":lista1,"suma1":c1,"suma":b1})




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
            
            return render(request,"pregleddatum.html",{"datum":result})
         

def manage(request):
    return render(request,'manageparking.html')
def dodaj1(request):
    return render(request,'dodaj.html')



def dodaj(request):
    
    
    
    if request.method=="POST":
        naziv=request.POST['naziv']
        lista=Parking.objects.all()
        lista1=Parking2.objects.all()
        a=Parking.objects.filter(NazivMjesta=naziv).count()
        b=Parking.objects.filter(NazivMjesta=naziv).count()
        sumres=Parkingmjesto.objects.all().aggregate(Sum('KM'))
        if a > 0 or b > 0:
            messages.success(request,"Parking Mjesto već postoji!")
            sql="select NazivMjesta from parkingapp_parking"
    
            mycursor.execute(sql)
            nazivparkinga = mycursor.fetchall()
                
            sql="select NazivMjesta from parkingapp_parking2"
                
            mycursor.execute(sql)
            nazivparkinga2 = mycursor.fetchall()
            


            
            sumaparking1=[]
            
            
                

        
                
                
                    
            sql="Select BrojMjesta from parkingapp_parking"
            mycursor.execute(sql)
            pp=mycursor.fetchall()
            i=0
            b1=[]
            bb1=[]
            for ss in nazivparkinga:
                counter=0
                counter=Parkingmjesto.objects.filter(ParkingMjesto=ss[0],Datum=Datum,VrijemeOdjave__gte=Vrijeme).count()
                bb1.append(counter)
            c1=[]
            broj1=0
            for xs in pp:
                number=0
                number=xs[0]-bb1[broj1]
                b1.append(number)
                broj1=broj1 + 1
            

            sql="Select BrojMjesta from parkingapp_parking2"
            mycursor.execute(sql)
            pp1=mycursor.fetchall()
            ii=0

            cc1=[]
            

            for s in nazivparkinga2:
                counter=0
                counter=Parkingmjesto.objects.filter(ParkingMjesto=s[0],Datum=Datum,VrijemeOdjave__gte=Vrijeme).count()
                cc1.append(counter)
            c1=[]
            broj=0
            for xx in pp1:
                number=0
                number=xx[0]-cc1[broj]
                c1.append(number)
                broj=broj + 1
            return render(request,"dodaj.html",{"lista":lista,"lista1":lista1,"suma":b1,"suma1":c1,"ukupno":sumres["KM__sum"]})

        if request.POST['zona'] == "zona1":
            lista=Parking.objects.all()
            lista1=Parking2.objects.all()
            sql="insert into parkingapp_parking (NazivMjesta,BrojMjesta) values (%s,%s)"
            val=(request.POST['naziv'],request.POST['broj'])
            mycursor.execute(sql,val)
            mydb.commit()

            messages.success(request,"Uspiješno ste dodali parking mjesto!")
            sql="select NazivMjesta from parkingapp_parking"
    
            mycursor.execute(sql)
            nazivparkinga = mycursor.fetchall()
                
            sql="select NazivMjesta from parkingapp_parking2"
                
            mycursor.execute(sql)
            nazivparkinga2 = mycursor.fetchall()
            


            
            sumaparking1=[]
            
            
                

        
                
                
                    
            sql="Select BrojMjesta from parkingapp_parking"
            mycursor.execute(sql)
            pp=mycursor.fetchall()
            i=0
            b1=[]
            bb1=[]
            for ss in nazivparkinga:
                counter=0
                counter=Parkingmjesto.objects.filter(ParkingMjesto=ss[0],Datum=Datum,VrijemeOdjave__gte=Vrijeme).count()
                bb1.append(counter)
            c1=[]
            broj1=0
            for xs in pp:
                number=0
                number=xs[0]-bb1[broj1]
                b1.append(number)
                broj1=broj1 + 1
            

            sql="Select BrojMjesta from parkingapp_parking2"
            mycursor.execute(sql)
            pp1=mycursor.fetchall()
            ii=0

            cc1=[]
            

            for s in nazivparkinga2:
                counter=0
                counter=Parkingmjesto.objects.filter(ParkingMjesto=s[0],Datum=Datum,VrijemeOdjave__gte=Vrijeme).count()
                cc1.append(counter)
            c1=[]
            broj=0
            for xx in pp1:
                number=0
                number=xx[0]-cc1[broj]
                c1.append(number)
                broj=broj + 1
            
            sumres=Parkingmjesto.objects.all().aggregate(Sum('KM'))
            return render(request,'listaparkinga.html',{"lista":lista,"lista1":lista1,"suma":b1,"suma1":c1,"ukupno":sumres["KM__sum"]})
        if request.POST['zona'] == "zona2":
            lista=Parking.objects.all()
            lista1=Parking2.objects.all()
            sql="insert into parkingapp_parking2 (NazivMjesta,BrojMjesta) values (%s,%s)"
            val=(request.POST['naziv'],request.POST['broj'])
            mycursor.execute(sql,val)
            mydb.commit()
            messages.success(request,"Uspiješno ste dodali parking mjesto!")
            sql="select NazivMjesta from parkingapp_parking"
    
            mycursor.execute(sql)
            nazivparkinga = mycursor.fetchall()
                
            sql="select NazivMjesta from parkingapp_parking2"
                
            mycursor.execute(sql)
            nazivparkinga2 = mycursor.fetchall()
            


            
            sumaparking1=[]
            
            
                

        
                
                
                    
            sql="Select BrojMjesta from parkingapp_parking"
            mycursor.execute(sql)
            pp=mycursor.fetchall()
            i=0
            b1=[]
            bb1=[]
            for ss in nazivparkinga:
                counter=0
                counter=Parkingmjesto.objects.filter(ParkingMjesto=ss[0],Datum=Datum,VrijemeOdjave__gte=Vrijeme).count()
                bb1.append(counter)
            c1=[]
            broj1=0
            for xs in pp:
                number=0
                number=xs[0]-bb1[broj1]
                b1.append(number)
                broj1=broj1 + 1
            

            sql="Select BrojMjesta from parkingapp_parking2"
            mycursor.execute(sql)
            pp1=mycursor.fetchall()
            ii=0

            cc1=[]
            

            for s in nazivparkinga2:
                counter=0
                counter=Parkingmjesto.objects.filter(ParkingMjesto=s[0],Datum=Datum,VrijemeOdjave__gte=Vrijeme).count()
                cc1.append(counter)
            c1=[]
            broj=0
            for xx in pp1:
                number=0
                number=xx[0]-cc1[broj]
                c1.append(number)
                broj=broj + 1
            sumres=Parkingmjesto.objects.all().aggregate(Sum('KM'))
            return render(request,'listaparkinga.html',{"lista":lista,"lista1":lista1,"suma":b1,"suma1":c1,"ukupno":sumres["KM__sum"]})
        

def obrisi1(request):
    lista=Parking.objects.all()
    lista1=Parking2.objects.all()
    return render(request,'obrisi.html',{"lista":lista,"lista1":lista1})
   

def obrisi(request):
    if request.method=="POST":
        
        if request.POST['zona'] == "zona1":
            value=request.POST['naziv']
            instance = Parking.objects.get(NazivMjesta=value)
            instance.delete()
            lista=Parking.objects.all()
            lista1=Parking2.objects.all()
            sql="select NazivMjesta from parkingapp_parking"
    
            mycursor.execute(sql)
            nazivparkinga = mycursor.fetchall()
                
            sql="select NazivMjesta from parkingapp_parking2"
                
            mycursor.execute(sql)
            nazivparkinga2 = mycursor.fetchall()
            


            
            sumaparking1=[]
            
            
                

        
                
                
                    
            sql="Select BrojMjesta from parkingapp_parking"
            mycursor.execute(sql)
            pp=mycursor.fetchall()
            i=0
            b1=[]
            bb1=[]
            for ss in nazivparkinga:
                counter=0
                counter=Parkingmjesto.objects.filter(ParkingMjesto=ss[0],Datum=Datum,VrijemeOdjave__gte=Vrijeme).count()
                bb1.append(counter)
            c1=[]
            broj1=0
            for xs in pp:
                number=0
                number=xs[0]-bb1[broj1]
                b1.append(number)
                broj1=broj1 + 1
            

            sql="Select BrojMjesta from parkingapp_parking2"
            mycursor.execute(sql)
            pp1=mycursor.fetchall()
            ii=0

            cc1=[]
            

            for s in nazivparkinga2:
                counter=0
                counter=Parkingmjesto.objects.filter(ParkingMjesto=s[0],Datum=Datum,VrijemeOdjave__gte=Vrijeme).count()
                cc1.append(counter)
            c1=[]
            broj=0
            for xx in pp1:
                number=0
                number=xx[0]-cc1[broj]
                c1.append(number)
                broj=broj + 1
            messages.success(request,"Uspiješno ste obrisali parking mjesto !")
            sumres=Parkingmjesto.objects.all().aggregate(Sum('KM'))
            return render(request,'listaparkinga.html',{"lista":lista,"lista1":lista1,"suma":b1,"suma1":c1,"ukupno":sumres["KM__sum"]})
        if request.POST['zona'] == "zona2":
            value=request.POST['naziv']
            instance = Parking2.objects.get(NazivMjesta=value)
            instance.delete()
            lista=Parking.objects.all()
            lista1=Parking2.objects.all()
            sql="select NazivMjesta from parkingapp_parking"
    
            mycursor.execute(sql)
            nazivparkinga = mycursor.fetchall()
                
            sql="select NazivMjesta from parkingapp_parking2"
                
            mycursor.execute(sql)
            nazivparkinga2 = mycursor.fetchall()
            


            
            sumaparking1=[]
            
            
                

        
                
                
                    
            sql="Select BrojMjesta from parkingapp_parking"
            mycursor.execute(sql)
            pp=mycursor.fetchall()
            i=0
            b1=[]
            bb1=[]
            for ss in nazivparkinga:
                counter=0
                counter=Parkingmjesto.objects.filter(ParkingMjesto=ss[0],Datum=Datum,VrijemeOdjave__gte=Vrijeme).count()
                bb1.append(counter)
            c1=[]
            broj1=0
            for xs in pp:
                number=0
                number=xs[0]-bb1[broj1]
                b1.append(number)
                broj1=broj1 + 1
            

            sql="Select BrojMjesta from parkingapp_parking2"
            mycursor.execute(sql)
            pp1=mycursor.fetchall()
            ii=0

            cc1=[]
            

            for s in nazivparkinga2:
                counter=0
                counter=Parkingmjesto.objects.filter(ParkingMjesto=s[0],Datum=Datum,VrijemeOdjave__gte=Vrijeme).count()
                cc1.append(counter)
            c1=[]
            broj=0
            for xx in pp1:
                number=0
                number=xx[0]-cc1[broj]
                c1.append(number)
                broj=broj + 1
            sumres=Parkingmjesto.objects.all().aggregate(Sum('KM'))
            messages.success(request,"Uspiješno ste obrisali parking mjesto !")
            return render(request,'listaparkinga.html',{"lista":lista,"lista1":lista1,"suma":b1,"suma1":c1,"ukupno":sumres["KM__sum"]})

def uredi1(request):
    lista=Parking.objects.all()
    lista1=Parking2.objects.all()
    sql="select NazivMjesta from parkingapp_parking"
    
    mycursor.execute(sql)
    nazivparkinga = mycursor.fetchall()
                
    sql="select NazivMjesta from parkingapp_parking2"
                
    mycursor.execute(sql)
    nazivparkinga2 = mycursor.fetchall()
    sumaparking1=[]
            
            
                

        
                
                
                    
    sql="Select BrojMjesta from parkingapp_parking"
    mycursor.execute(sql)
    pp=mycursor.fetchall()
    i=0
    b1=[]
    bb1=[]
    for ss in nazivparkinga:
        counter=0
        counter=Parkingmjesto.objects.filter(ParkingMjesto=ss[0],Datum=Datum,VrijemeOdjave__gte=Vrijeme).count()
        bb1.append(counter)
    c1=[]
    broj1=0
    for xs in pp:
        number=0
        number=xs[0]-bb1[broj1]
        b1.append(number)
        broj1=broj1 + 1
    

    sql="Select BrojMjesta from parkingapp_parking2"
    mycursor.execute(sql)
    pp1=mycursor.fetchall()
    ii=0

    cc1=[]
    

    for s in nazivparkinga2:
        counter=0
        counter=Parkingmjesto.objects.filter(ParkingMjesto=s[0],Datum=Datum,VrijemeOdjave__gte=Vrijeme).count()
        cc1.append(counter)
    c1=[]
    broj=0
    for xx in pp1:
        number=0
        number=xx[0]-cc1[broj]
        c1.append(number)
        broj=broj + 1
    return render(request,'uredi.html',{"lista":lista,"lista1":lista1,"suma":b1,"suma1":c1})

def uredi(request):
    





    sql="select NazivMjesta from parkingapp_parking"
    
    mycursor.execute(sql)
    nazivparkinga = mycursor.fetchall()
        
    sql="select NazivMjesta from parkingapp_parking2"
        
    mycursor.execute(sql)
    nazivparkinga2 = mycursor.fetchall()
    


    
    sumaparking1=[]
    
    
        

   
        
        
            
    sql="Select BrojMjesta from parkingapp_parking"
    mycursor.execute(sql)
    pp=mycursor.fetchall()
    i=0
    b1=[]
    bb1=[]
    for ss in nazivparkinga:
        counter=0
        counter=Parkingmjesto.objects.filter(ParkingMjesto=ss[0],Datum=Datum,VrijemeOdjave__gte=Vrijeme).count()
        bb1.append(counter)
    c1=[]
    broj1=0
    for xs in pp:
        number=0
        number=xs[0]-bb1[broj1]
        b1.append(number)
        broj1=broj1 + 1
    

    sql="Select BrojMjesta from parkingapp_parking2"
    mycursor.execute(sql)
    pp1=mycursor.fetchall()
    ii=0

    cc1=[]
    

    for s in nazivparkinga2:
        counter=0
        counter=Parkingmjesto.objects.filter(ParkingMjesto=s[0],Datum=Datum,VrijemeOdjave__gte=Vrijeme).count()
        cc1.append(counter)
    c1=[]
    broj=0
    for xx in pp1:
        number=0
        number=xx[0]-cc1[broj]
        c1.append(number)
        broj=broj + 1
    if request.method=="POST":
        if request.POST['zona']=="zona1":
            Parking.objects.filter(NazivMjesta=request.POST['naziv']).update(NazivMjesta=request.POST['naziv1'],BrojMjesta=request.POST['broj'])
            lista=Parking.objects.all()
            lista1=Parking2.objects.all()
            sumres=Parkingmjesto.objects.all().aggregate(Sum('KM'))
            return render(request,'listaparkinga.html',{"lista":lista,"lista1":lista1,"suma":b1,"suma1":c1,"ukupno":sumres["KM__sum"]})
        if request.POST['zona']=="zona2":
            Parking2.objects.filter(NazivMjesta=request.POST['naziv']).update(NazivMjesta=request.POST['naziv1'],BrojMjesta=request.POST['broj'])
            lista=Parking.objects.all()
            lista1=Parking2.objects.all()
            sumres=Parkingmjesto.objects.all().aggregate(Sum('KM'))
            return render(request,'listaparkinga.html',{"lista":lista,"lista1":lista1,"suma":b1,"suma1":c1,"ukupno":sumres["KM__sum"]})
    
        
def adminpanel(request):
    return render(request,'adminpanel.html')

def listaadmina(request):
    lista=AdminPanel.objects.all()
    return render(request,'listaadmina.html',{"lista":lista})
def urediadmina(request):
    lista=AdminPanel.objects.all()

    return render(request,"urediadmina.html",{"lista":lista})

def adminedit(request):
    key=25852
    key2=int(request.POST['Key'])
    if request.method=="POST":
        operacija=request.POST['operacija']
        if key == key2:
        

            if operacija=="Obriši":
                value=request.POST['Email']
                instance = AdminPanel.objects.get(EmailAdmina=value)
                instance.delete()
                
                lista=AdminPanel.objects.all()
                messages.success(request,"Uspiješno ste obrisali admina")
                return render(request,"listaadmina.html",{"lista":lista})
            if operacija=="Dodaj":
                Email=request.POST['Email']
                Pwd=request.POST['Pwd']
                AdminPanel(EmailAdmina=Email,PwdAdmina=Pwd).save()
                
                lista=AdminPanel.objects.all()
                messages.success(request,"Uspiješno ste dodali admina")
                return render(request,"listaadmina.html",{"lista":lista})
        else:
            messages.success(request,"Nemate pristup,pogrešan ključ !")
            lista=AdminPanel.objects.all()
            return render(request,"urediadmina.html",{"lista":lista})