from django.contrib import messages
from django.shortcuts import redirect, render, get_object_or_404
from .models import Room
from .models import Guest, Booking, Room
from django.urls import reverse
from datetime import datetime
from django.http import HttpResponse, HttpResponseRedirect
from django.db.models import Q


# Create your views here.


# def reservation(request):
#     room_id = request.GET.get('room_id')
#     start_date = request.GET.get('start')
#     end_date = request.GET.get('end')
    

    
#     room = None
#     if room_id:
#         room = get_object_or_404(Room, id=room_id)
    
#     context = {
#         'room': room,
#         'start_date': start_date,
#         'end_date': end_date
#     }
#     return render(request, 'reservation/reservation.html', context)


def reservation(request):
    room_id = request.GET.get('room_id')
    start_date = request.GET.get('start')
    end_date = request.GET.get('end')

    room = get_object_or_404(Room, id=room_id)

    if start_date and end_date:
        # Конвертируем строки в объекты даты
        start_date_obj = datetime.strptime(start_date, "%d/%m/%Y").date()
        end_date_obj = datetime.strptime(end_date, "%d/%m/%Y").date()

        # Проверяем, свободен ли номер
        overlapping_bookings = Booking.objects.filter(
            room_id=room_id,
            check_in__lte=end_date_obj,
            check_out__gte=start_date_obj
        ).exists()

        if overlapping_bookings:
            # Если номер занят, передаем контекст для отображения блока "номер занят"
            context = {'room_booked': True}
            return render(request, 'reservation/reservation.html', context)

    if request.method == 'POST':
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')

        # Конвертируем строки в объекты даты
        start_date_obj = datetime.strptime(start_date, "%d/%m/%Y").date()
        end_date_obj = datetime.strptime(end_date, "%d/%m/%Y").date()

        # Проверяем, свободен ли номер
        overlapping_bookings = Booking.objects.filter(
            room=room,
            check_in__lte=end_date_obj,
            check_out__gte=start_date_obj
        ).exists()

        if overlapping_bookings:
            # Если есть пересечение существующих броней, возвращаем ошибку
            return HttpResponse('Номер занят на выбранные даты, пожалуйста, выберите другие даты.', status=400)

        # Создаем бронь, если номер свободен
        guest = Guest(
            first_name=request.POST.get('first_name'),
            last_name=request.POST.get('last_name'),
            passport_number=request.POST.get('passport_number'),
            city_from=request.POST.get('arrival_city')
        )
        guest.save()

        booking = Booking(
            room=room,
            check_in=start_date_obj,
            check_out=end_date_obj,
            guest=guest
        )
        booking.save()

        # messages.success(request, 'Бронирование успешно создано.')
        return redirect('reservation:reservation_confirmation')  # Use the namespace

    context = {
        'room': room,
        'start_date': start_date,
        'end_date': end_date
    }
    return render(request, 'reservation/reservation.html', context)


def reservation_confirmation(request):
    # Here you can add context or session data to show on the confirmation page if needed
    return render(request, 'reservation/confirmation.html')