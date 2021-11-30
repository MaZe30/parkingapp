from django.http import request
import mysql.connector
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",
    database="parking"
    

)




mycursor=mydb.cursor()
from django.shortcuts import render
from parkingapp.models import Newuser
from django.contrib import messages
from parkingapp.models import Parkingmjesto
from parkingapp.models import PlacanjeSms
from parkingapp.models import PlacanjeKarticno
from parkingapp.models import Rezervacija
from datetime import date,datetime
import time
today=date.today()
now = datetime.now()



Brodac=30 
Alipašina=26
Branilaca=20
Musala=20
Buka=36
Ćemaluša=20
Danijela=28
Despićeva=20
Dzenetiča=40
Džidžikovac=20


Augusta=30
Autobuska=36
Dolac=34
Dolina=20
Džemala=20
Franca=28
Franje=24
Hazima=20
Herceg=30
Koste=20
  
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
    

def delete(request):
    if request.method=='POST':    
        username1=request.POST['Email12']
        
        sql="DELETE FROM parkingapp_newuser WHERE Email = 'username1'  "
        
        mycursor.execute(sql)
        mydb.commit()
        

        messages.success(request,"Korisnik obrisan")
        return render(request,'listausera.html')
        
        
            
    



def parkingspot(request):
    if request.method=="POST":
        
        ParkingMjesto=request.POST['zona1']
        Registracija=request.POST['tablica']
        Username=request.session['user']
        Satnica=request.POST['Satnica']
        Datum = today.strftime("%m/%d/%y")
        Vrijeme=now.strftime("%H:%M:%S")
        

        if ParkingMjesto == "Brodac":
            global Brodac
            

            Brodac=Brodac - 1
            
            Parkingmjesto(ParkingMjesto=ParkingMjesto,Registracija=Registracija,Username=Username,Datum=Datum,Vrijeme=Vrijeme,Satnica=Satnica).save()
            
            
            return render(request,'birajplacanje.html',{"username":Username})
        
            
            
        if ParkingMjesto == "Musala":
            global Musala
            

            Musala=Musala - 1
            
            Parkingmjesto(ParkingMjesto=ParkingMjesto,Registracija=Registracija,Username=Username,Datum=Datum,Vrijeme=Vrijeme,Satnica=Satnica).save()
            
            return render(request,'birajplacanje.html',{"username":Username,"Musala":Musala})
        if ParkingMjesto == "Branilaca_Sarajeva":
            global Branilaca
            

            Branilaca=Branilaca - 1
            
            Parkingmjesto(ParkingMjesto=ParkingMjesto,Registracija=Registracija,Username=Username,Datum=Datum,Vrijeme=Vrijeme,Satnica=Satnica).save()
            
            return render(request,'birajplacanje.html',{"username":Username})
        if ParkingMjesto == "Alipašina":
            global Alipašina
            

            Alipašina=Alipašina - 1
            request.session['ppp']=Alipašina
            
            Parkingmjesto(ParkingMjesto=ParkingMjesto,Registracija=Registracija,Username=Username,Datum=Datum,Vrijeme=Vrijeme,Satnica=Satnica).save()
            
            return render(request,'birajplacanje.html',{"username":Username})
        if ParkingMjesto == "Buka":
            global Buka
            

            Buka=Buka - 1
            
            Parkingmjesto(ParkingMjesto=ParkingMjesto,Registracija=Registracija,Username=Username,Datum=Datum,Vrijeme=Vrijeme,Satnica=Satnica).save()
            
            return render(request,'birajplacanje.html',{"username":Username})
        if ParkingMjesto == "Ćemaluša":
            global Ćemaluša
            

            Ćemaluša=Ćemaluša- 1
            
            Parkingmjesto(ParkingMjesto=ParkingMjesto,Registracija=Registracija,Username=Username,Datum=Datum,Vrijeme=Vrijeme,Satnica=Satnica).save()
            
            return render(request,'birajplacanje.html',{"username":Username})
        if ParkingMjesto == "Danijela_Ozme":
            global Danijela
            

            Danijela=Danijela - 1
            
            Parkingmjesto(ParkingMjesto=ParkingMjesto,Registracija=Registracija,Username=Username,Datum=Datum,Vrijeme=Vrijeme,Satnica=Satnica).save()
            
            return render(request,'birajplacanje.html',{"username":Username})
        if ParkingMjesto == "Despićeva":
            global Despićeva
            

            Despićeva=Despićeva - 1
            
            Parkingmjesto(ParkingMjesto=ParkingMjesto,Registracija=Registracija,Username=Username,Datum=Datum,Vrijeme=Vrijeme,Satnica=Satnica).save()
            
            return render(request,'birajplacanje.html',{"username":Username})
        if ParkingMjesto == "Dženetića_čikma":
            global Dzenetiča
            

            Dzenetiča=Dzenetiča - 1
            
            Parkingmjesto(ParkingMjesto=ParkingMjesto,Registracija=Registracija,Username=Username,Datum=Datum,Vrijeme=Vrijeme,Satnica=Satnica).save()
            
            return render(request,'birajplacanje.html',{"username":Username})
        if ParkingMjesto == "Džidžikovac":
            global Džidžikovac
            

            Džidžikovac=Džidžikovac - 1
            
            
            Parkingmjesto(ParkingMjesto=ParkingMjesto,Registracija=Registracija,Username=Username,Datum=Datum,Vrijeme=Vrijeme,Satnica=Satnica).save()
            
            return render(request,'birajplacanje.html',{"username":Username})
            
        
            

def parkingspot1(request):
    if request.method=="POST":
        ParkingMjesto=request.POST['zona2'] 
        Registracija=request.POST['tablica']
        Username=request.session['user']
        Datum = today.strftime("%m/%d/%y")
        Vrijeme=now.strftime("%H:%M:%S")
        Satnica=request.POST['Satnica']
        

        
        if ParkingMjesto == "Augusta":
            global Augusta
            

            Augusta=Augusta - 1
            
            Parkingmjesto(ParkingMjesto=ParkingMjesto,Registracija=Registracija,Username=Username,Datum=Datum,Vrijeme=Vrijeme,Satnica=Satnica).save()
            
            return render(request,'birajplacanje.html',{"username":Username})
        if ParkingMjesto == "Autobuska_stanica_Pošta":
            global Autobuska
            

            Autobuska=Autobuska- 1
            
            Parkingmjesto(ParkingMjesto=ParkingMjesto,Registracija=Registracija,Username=Username,Datum=Datum,Vrijeme=Vrijeme,Satnica=Satnica).save()
            
            return render(request,'birajplacanje.html',{"username":Username,"Musala":Musala})
        if ParkingMjesto == "Dolac_Malta_Pošta":
            global Dolac
            

            Dolac=Dolac - 1
            
            Parkingmjesto(ParkingMjesto=ParkingMjesto,Registracija=Registracija,Username=Username,Datum=Datum,Vrijeme=Vrijeme,Satnica=Satnica).save()
            
            return render(request,'birajplacanje.html',{"username":Username})
        if ParkingMjesto == "Dolina":
            global Dolina
            

            Dolina=Dolina - 1
            
            
            Parkingmjesto(ParkingMjesto=ParkingMjesto,Registracija=Registracija,Username=Username,Datum=Datum,Vrijeme=Vrijeme,Satnica=Satnica).save()
            
            return render(request,'birajplacanje.html',{"username":Username})
        if ParkingMjesto == "Džemala_Bijedića":
            global Džemala
            

            Džemala=Džemala - 1
            
            Parkingmjesto(ParkingMjesto=ParkingMjesto,Registracija=Registracija,Username=Username,Datum=Datum,Vrijeme=Vrijeme,Satnica=Satnica).save()
            
            return render(request,'birajplacanje.html',{"username":Username})
        if ParkingMjesto == "Franca_Lehara":
            global Franca
            

            Franca=Franca - 1
            
            Parkingmjesto(ParkingMjesto=ParkingMjesto,Registracija=Registracija,Username=Username,Datum=Datum,Vrijeme=Vrijeme,Satnica=Satnica).save()
            
            return render(request,'birajplacanje.html',{"username":Username})
        if ParkingMjesto == "Franje_Račkog":
            global Franje
            

            Franje=Franje - 1
            
            Parkingmjesto(ParkingMjesto=ParkingMjesto,Registracija=Registracija,Username=Username,Datum=Datum,Vrijeme=Vrijeme,Satnica=Satnica).save()
            
            return render(request,'birajplacanje.html',{"username":Username})
        if ParkingMjesto == "Hazima_Šabanovića":
            global Hazima
            

            Hazima=Hazima - 1
            
            Parkingmjesto(ParkingMjesto=ParkingMjesto,Registracija=Registracija,Username=Username,Datum=Datum,Vrijeme=Vrijeme,Satnica=Satnica).save()
            
            return render(request,'birajplacanje.html',{"username":Username})
        if ParkingMjesto == "Herceg_Stjepana":
            global Herceg
            

            Herceg=Herceg - 1
            
            Parkingmjesto(ParkingMjesto=ParkingMjesto,Registracija=Registracija,Username=Username,Datum=Datum,Vrijeme=Vrijeme,Satnica=Satnica).save()
            
            return render(request,'birajplacanje.html',{"username":Username})
        if ParkingMjesto == "Koste_Hermana":
            global Koste
            

            Koste=Koste - 1
            
            
            Parkingmjesto(ParkingMjesto=ParkingMjesto,Registracija=Registracija,Username=Username,Datum=Datum,Vrijeme=Vrijeme,Satnica=Satnica).save()
            
            return render(request,'birajplacanje.html',{"username":Username})
    
def sms(request):
    
        if request.method=='POST':
            BrojTelefona=request.POST['BrojTelefona']
            
            Username=request.session['user']
            Datum = today.strftime("%m/%d/%y")
            Vrijeme=now.strftime("%H:%M:%S")
            PlacanjeSms(BrojTelefona=BrojTelefona,Username=Username,Datum=Datum,Vrijeme=Vrijeme).save()
            messages.success(request,'Uspiješno ste uplatili '+request.POST['Satnica']+' sati/a parkinga')
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
    
def zona1(request):
    return render(request,'parkingmjesto1.html',{"username": request.session['user']})

def zona2(request):
    return render(request,'parkingmjesto2.html',{"username": request.session['user']})

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
    
    
    return render(request,'listaparkinga.html',{"ppp":Alipašina,"p2":Brodac,"p3":Branilaca,"Musala":Musala,"p5":Buka,"p6":Ćemaluša,"p7":Danijela,"p8":Despićeva,"p9":Dzenetiča,"p10":Džidžikovac,"p11":Augusta,"p12":Autobuska,"p13":Dolac,"p14":Dolina,"p15":Džemala,"p16":Franca,"p17":Franje,"p18":Hazima,"p19":Herceg,"p20":Koste})



def delete(request):
    if request.method=="POST":
        value=request.POST['Email12']
        data_to_be_deleted = Newuser.objects.get(Email = value)
        data_to_be_deleted.delete()
        messages.success(request,"Uspiješno ste obrisali korisnika")
        return render(request,'admin.html')


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
    return render(request,'pregleduserparkinga.html',{'Parkingmjesto': result,"Parkingmjesto1":result1,"Parkingmjesto2":result2,"username":username,"rezervacija":result3})
    
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
    
    
    return render(request,'brojmjesta.html',{"ppp":Alipašina,"p2":Brodac,"p3":Branilaca,"Musala":Musala,"p5":Buka,"p6":Ćemaluša,"p7":Danijela,"p8":Despićeva,"p9":Dzenetiča,"p10":Džidžikovac,"p11":Augusta,"p12":Autobuska,"p13":Dolac,"p14":Dolina,"p15":Džemala,"p16":Franca,"p17":Franje,"p18":Hazima,"p19":Herceg,"p20":Koste,"username":username})
def datum(request):
    return render(request,"pregledpodatumu.html")

def datum2(request):
    if request.method=='POST': 
        datum=request.POST['datum']   
        
        result=Parkingmjesto.objects.all().filter(Datum=datum)
        return render(request,"pregleddatum.html",{"datum":result})
   