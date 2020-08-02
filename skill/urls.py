from django.urls import path
from . import views

urlpatterns = [
    path('', views.skill, name="skill"),
    path('about/', views.about, name="about")
]
