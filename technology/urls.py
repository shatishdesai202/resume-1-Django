from django.urls import path
from . import views

urlpatterns = [
    path('techno/', views.tech, name="tech")
]
