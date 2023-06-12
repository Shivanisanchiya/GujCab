from django.shortcuts import render
import datetime
from datetime import timedelta
from .models import Oneway,RoundTrip,Packages,Cabs
from django.shortcuts import redirect
# Create your views here.

def index(request):
    return render(request,"index.html")

def oneway(request):
    package = Packages.objects.all()
    if request.method == "POST":
        name = request.POST["name"]
        mo_no = request.POST["no"]
        fromcity = request.POST["FromCity"]
        tocity = request.POST["ToCity"]
        date = request.POST["date"]
        starttime = request.POST["time"]
        cabchoice = request.POST["cab"]
        new_data = Oneway(Name=name, Mo_No=mo_no, FromCity=fromcity, Tocity=tocity, date=date, StartTime=starttime,CabChoice=cabchoice)
        new_data.save()
        return redirect(msg)
    return render(request,"oneway.html",{'package':package})

def roundtrip(request):
    package = Packages.objects.all()
    if request.method == "POST":
        name = request.POST["name"]
        mo_no = request.POST["no"]
        fromcity = request.POST["FromCity"]
        tocity = request.POST["ToCity"]
        journeydate = request.POST["date"]
        returndate = request.POST["datereturn"]
        starttime = request.POST["time"]
        cabchoice = request.POST["cab"]
        new_data = RoundTrip(name=name, mo_No=mo_no, fromCity=fromcity, toCity=tocity, dateOfJourney=journeydate, 
        dateOfReturn=returndate,startTime=starttime,cabChoice=cabchoice)
        new_data.save()
        return redirect(msg)
    return render(request,"roundtrip.html",{'package':package})

def cabs(request):
    data = Cabs.objects.all()
    return render(request,"cabs.html",{'data':data})

def msg(request):
    n=45
    dt = datetime.datetime.now() 
    ft = dt + timedelta(minutes=n)
    future_time = ft.strftime('%H:%M:%S.%f')
    # print(ft)
    return render(request,"msg.html",{'ft':ft})