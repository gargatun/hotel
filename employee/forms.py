from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import get_user_model
from reservation.models import Guest
from rooms.models import Room

class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Логин'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Пароль'}))

    class Meta:
        model = get_user_model()
        fields = ['username', 'password']




class CityForm(forms.Form):
    city = forms.ChoiceField(
        label='Город:',
        widget=forms.Select(attrs={'class': 'form-control'}),  # Add Bootstrap class
        choices=[]
    )

    def __init__(self, *args, **kwargs):
        super(CityForm, self).__init__(*args, **kwargs)
        unique_cities = Guest.objects.order_by('city_from').values_list('city_from', flat=True).distinct()
        city_choices = [(city, city) for city in unique_cities]
        city_choices.insert(0, ('', 'Выберите город'))  # Placeholder text
        self.fields['city'].choices = city_choices


class CleaningLookupForm(forms.Form):
    guest = forms.ModelChoiceField(
        queryset=Guest.objects.all(),
        widget=forms.Select(attrs={'class': 'form-select'}),  # Use 'form-select' for dropdowns
        label='Гость:'
    )
    date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),  # Ensure 'form-control' is used for input types
        label='Дата:'
    )

class RoomTypeForm(forms.Form):
    room_type = forms.ChoiceField(choices=Room.ROOM_TYPES, label='Тип номера', required=True)

    def __init__(self, *args, **kwargs):
        super(RoomTypeForm, self).__init__(*args, **kwargs)
        self.fields['room_type'].widget.attrs.update({'class': 'form-select'})