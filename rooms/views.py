from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render, redirect

from rooms.models import Room


# Create your views here.
def index(request):
    # Получаем по одному номеру каждого типа
    single_room = Room.objects.filter(room_type='single').first()
    double_room = Room.objects.filter(room_type='double').first()
    triple_room = Room.objects.filter(room_type='triple').first()

    rooms = [room for room in [single_room, double_room, triple_room] if room is not None]

    return render(request, 'rooms/index.html', {'rooms': rooms})


def rooms(request):
    page = request.GET.get('page', 1)
    order_by = request.GET.get('order_by', 'default')
    selected_room_types = request.GET.getlist('room_type')

    rooms = Room.objects.filter(is_available=True)
    if selected_room_types:
        rooms = rooms.filter(room_type__in=selected_room_types)

    if order_by != 'default':
        rooms = rooms.order_by(order_by)

    paginator = Paginator(rooms, 3)
    current_page = paginator.page(int(page))

    context = {
        "title": "Rooms Catalog",
        "rooms": current_page,
        "selected_room_types": selected_room_types,
        "room_types": Room.ROOM_TYPES,  # Add this line
        "order_by": order_by  # Добавьте order_by в контекст
    }
    return render(request, "rooms/rooms.html", context)


