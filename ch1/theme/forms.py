from django import forms
from .models import Booking


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = [
            'name',
            'phone',
            'numPeople',
            'depositWay',
        ]
        widgets = {
            'name':forms.TextInput(
                attrs={
                    'style': 'width:100%',
                    'class': 'form-control',
                }
            ),
            'phone': forms.TextInput(
                attrs={
                    'style': 'width:100%',
                    'class': 'form-control',
                }
            ),
            'numPeople': forms.Select(
                attrs={
                    'style': 'width:100%',
                    'class': 'form-control',
                    'onchange': 'price_change();',
                    'name': 'numPeople'
                }
            ),
            'depositWay': forms.Select(
                attrs={
                    'style': 'width:100%',
                    'class': 'form-control',
                }
            )
        }


