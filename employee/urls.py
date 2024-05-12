from django.urls import path
from employee import views
from django.contrib.auth.views import LogoutView


app_name = 'employee'

urlpatterns = [
    path('login/', views.LoginUser.as_view(), name='login'),
    path('', views.IndexView.as_view(), name='index'),  # Make sure this corresponds to `success_url`
    path('logout/', LogoutView.as_view(next_page='employee:index'), name='logout'),

]