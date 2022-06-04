from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns=[
    path('',views.index,name = 'index'),
    path('display/',views.display, name='display'),
    path('search/', views.search_results, name='search_results'),
    path('location/<location>/',views.location_results, name='location_results')
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)