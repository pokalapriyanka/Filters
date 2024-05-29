from django.shortcuts import render

# Create your views here.
import datetime
def filter(request):
    da=datetime.datetime.now()
    d={'data':'Hi pYThoN How aRE YoU','da':da ,'c':1}
    return render(request,'filter.html',d)


def userfilters(request):
    d={'data':'Hi pYThoN How aRE YoU'}
    return render(request,'userfilters.html',d)