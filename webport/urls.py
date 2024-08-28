from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("cv.html", views.cv, name="cv"),  
]
