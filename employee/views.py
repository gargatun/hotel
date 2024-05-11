from django.db.models import Sum
from django.shortcuts import redirect, render
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from employee.forms import LoginUserForm
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

from rooms.models import Room

from .forms import CityForm, CleaningLookupForm, RoomTypeForm
from reservation.models import Booking, Guest
from .models import CleaningSchedule
from django.utils.timezone import now


# Create your views here.

class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'employee/login.html'
    redirect_authenticated_user = False  # Allow authenticated users to see the login page
    success_url = reverse_lazy('employee:index')

    def get(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect(self.get_success_url())
        return super().get(request, *args, **kwargs)

		
class IndexView(LoginRequiredMixin, TemplateView):
    template_name = 'employee/index.html'
    login_url = '/employee/login/'  # Explcitly specify where to redirect unauthenticated users
    # redirect_field_name = 'next'  # This will append '?next=/employee/' to the login URL

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['city_form'] = CityForm(self.request.GET or None)
        context['cleaning_form'] = CleaningLookupForm()
        context['room_type_form'] = RoomTypeForm(self.request.GET or None)  # Add the RoomTypeForm to the context
        context['available_rooms_count'] = self.get_available_rooms_count()
        context['occupancy_rate'] = self.get_occupancy_rate()
        context['occupied_rooms_count'] = self.get_occupied_rooms_count()
        context['total_paid'] = self.get_total_paid()  # Add the total paid to the context

        if self.request.GET and context['room_type_form'].is_valid():
            room_type = context['room_type_form'].cleaned_data['room_type']
            rooms = Room.objects.filter(room_type=room_type, is_available=True)
            context['guests_in_rooms'] = Booking.objects.filter(room__in=rooms, check_in__lte=now().date(), check_out__gte=now().date()).select_related('guest', 'room')

        if self.request.GET and context['city_form'].is_valid():
            city = context['city_form'].cleaned_data.get('city')
            if city:
                context['guests'] = Guest.objects.filter(city_from=city)
        return context

    def post(self, request, *args, **kwargs):
        context = self.get_context_data()
        context['cleaning_form'] = CleaningLookupForm(request.POST)
        if context['cleaning_form'].is_valid():
            guest = context['cleaning_form'].cleaned_data['guest']
            date = context['cleaning_form'].cleaned_data['date']
            try:
                cleaning_entry = CleaningSchedule.objects.get(room__bookings__guest=guest, date=date)
                context['cleaner_info'] = f"{cleaning_entry.employee.full_name} убирался в этом номере - {cleaning_entry.date}"
            except CleaningSchedule.DoesNotExist:
                context['cleaner_info'] = "Информация об уборке на эту дату и для этого гостя не имеется."
        return self.render_to_response(context)


    def get_available_rooms_count(self):
        today = now().date()
        occupied_rooms = Booking.objects.filter(check_in__lte=today, check_out__gte=today).values_list('room', flat=True)
        return Room.objects.filter(is_available=True).exclude(id__in=occupied_rooms).count()

    def get_occupancy_rate(self):
        today = now().date()
        total_rooms = Room.objects.filter(is_available=True).count()
        occupied_rooms = Booking.objects.filter(check_in__lte=today, check_out__gte=today).count()
        occupancy_rate = (occupied_rooms / total_rooms) * 100 if total_rooms > 0 else 0
        return round(occupancy_rate)

    def get_occupied_rooms_count(self):
        today = now().date()
        return Booking.objects.filter(check_in__lte=today, check_out__gte=today).count()

    def get_total_paid(self):
        # Sum all full_price values where is_paid is True
        return Booking.objects.filter(is_paid=True).aggregate(Sum('full_price'))['full_price__sum'] or 0


