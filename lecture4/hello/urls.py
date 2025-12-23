from django.urls import path 
from . import views 

urlpatterns = [
    path("" , views.index , name="index"),
    path("<str:name>" , views.great , name="great"),
    path("saif" , views.saif , name="saif" ),
    path("david" , views.david , name="david")
]

