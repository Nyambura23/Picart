from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
import datetime as dte
from .models import User,Location,Image
from django.core.exceptions import ObjectDoesNotExist

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

def search_results(request):

    if 'image' in request.GET and request.GET["image"]:
        search_term = request.GET.get("image")
        searched_images = Image.search_by_title(search_term)
        message = f"{search_term}"

        return render(request, 'all-pics/search.html',{"message":message,"images": searched_images})

    else:
        message = "You haven't searched for any term"
        return render(request, 'all-pics/search.html',{"message":message})

def location_results(request, location):
    
    try:
        image_location = Image.filter_by_location(location)
        message = location
    except ObjectDoesNotExist:
        raise Http404()
    return render(request, 'location.html', {"location": image_location, 'message': location}) 

