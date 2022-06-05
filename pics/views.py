from django.shortcuts import render
from django.http import Http404
from .models import Image, Location
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.
def index(request):
    return render(request, 'index.html')

def display(request):
    images = Image.objects.all()
    location = Location.objects.all()
    return render(request, 'display.html',{"images":images, "location":location})

def search_results(request):
    if 'image' in request.GET and request.GET["image"]:
        search_term = request.GET.get("image")
        searched_images = Image.search_image(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"images": searched_images})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})

def location_results(request, location):
    
    try:
        image_location = Image.filter_by_location(location)
        message = location
    except ObjectDoesNotExist:
        raise Http404()
    return render(request, 'location.html', {"location": image_location, 'message': location}) 

