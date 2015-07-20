from django.conf.urls import url
from . import views

urlpatterns = [
  #  url(r'^avail_cars/(?P<start>(\d{4})-(\d{2})-(\d{2})_(\d{2}):(\d{2}):(\d{2}))/(?P<end>(\d{4})-(\d{2})-(\d{2})_(\d{2}):(\d{2}):(\d{2))/$', views.available_cars, name='avail_cars'),
    url(r'^avail_cars/(?P<start>\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\+\d{2}:\d{2})/(?P<end>\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\+\d{2}:\d{2})/$', views.available_cars, name='avail_cars'),
    url(r'^avail_cars/$', views.available_cars, name='avail_cars'),
]
                    
