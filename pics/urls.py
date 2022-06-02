from django.urls import path, re_path
from . import views


urlpatterns=[
    path('',views.welcome,name = 'welcome'),
    re_path('archives/(\d{4}-\d{2}-\d{2})/$',views.past_days_pics,name = 'pastPics'),
    path('search/', views.search_results, name='search_results')
]