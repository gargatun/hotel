from django.urls import path
from reservation import views


app_name = 'reservation'

urlpatterns = [
    path('', views.reservation, name='reservation'),
	path('confirmation/', views.reservation_confirmation, name='reservation_confirmation')
]
