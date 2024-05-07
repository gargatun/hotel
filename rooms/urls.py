from django.urls import path
from rooms import views


app_name = 'rooms'

urlpatterns = [
    path('', views.index, name='index'),
    path('rooms/', views.rooms, name='rooms'),
]




