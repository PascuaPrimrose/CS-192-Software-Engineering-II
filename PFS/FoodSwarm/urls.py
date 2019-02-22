from django.urls import path
from . import views
#defines the links in the application; where it goes
urlpatterns = [
    path('', views.home, name='FoodSwarm-Home'),
    path('about/', views.about, name='FoodSwarm-About'),
]
