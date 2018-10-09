from django.urls import path

from . import views

urlpatterns = [
    path('facility',views.times,name="timings")
]