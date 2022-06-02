from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
import datetime as dte
from .models import User

# Create your views here.
def welcome(request):
    return render(request, 'Welcome.html')

def pics_of_day(request):
    date = dte.date.today()
  
    return render(request, 'all-pics/today-pics.html', {"date": date,})


def past_days_pics(request,past_date):
    try:
        # Converts data from the string Url
        date = dte.datetime.strptime(past_date,'%Y-%m-%d').date()

    except ValueError:
     # Raise 404 error when ValueError is thrown
      raise Http404()
      assert False
      
    if date == dte.date.today():
        return redirect(pics_of_day)

    return render(request, 'all-pics/past-pics.html', {"date": date})

