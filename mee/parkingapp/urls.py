"""parkingapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from os import name
from parkingapp.models import PlacanjeKarticno, PlacanjeSms
from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.Indexpage),
    
    path('Registruj se',views.Userrreg,name='Reg'),
    path('Prijavi',views.back,name='back'),
    path("login",views.logincheck,name="loginpage"),
    path("me",views.parkingspot,name='me'),
    path("me1",views.parkingspot1,name='me1'),
    path("dalje",views.sms,name="sms"),
    path("card",views.kartica,name="kartica"),
    path("zona1",views.zona1,name='zona1'),
    path("zona2",views.zona2,name='zona2'),
    path("sms",views.placanje1,name='placanje1'),
    path("kartica",views.placanje2,name='placanje2'),
    path("useri",views.show,name='listausera'),
    path("delete",views.delete,name='delete'),
    path("listaparkinga",views.listaparkinga,name='listaparkinga'),
    path("parkiraj",views.parkiraj,name='parkiraj'),
    path("rezervisi",views.rezervisi,name='rezervisi'),
   
    path("rezervacija",views.rezervacija,name='rezervacija'),
    path("pregled",views.show1,name='userpregled'),
    path("pocetna",views.pocetna,name='pocetna'),
    path("odjava",views.odjava,name="odjava"),
    path("pocetna1",views.pocetna1,name='pocetna1'),
    path("rezervisi1",views.rezervacijaadmin,name="rezervisi1"),
    path("kod",views.kod,name="uplata"),
    path("kod1",views.kod1,name="kod"),
    path("broj",views.brojmjesta,name="broj"),
    path("datum",views.datum,name="datum"),
    path("datum1",views.datum2,name="datum1"),
    path("manage",views.manage,name="manage"),
    path("dodaj",views.dodaj,name="dodaj"),
    path("dodaj1",views.dodaj1,name="dodaj1"),
    path("obrisi1",views.obrisi1,name="obrisi1"),
    path("obrisi",views.obrisi,name="obrisii"),
    path("uredi1",views.uredi1,name="uredi1"),
    path("uredi",views.uredi,name="uredi")
    
    

    
    


]
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)
