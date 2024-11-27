from django.forms import ModelForm

from .models import Event
from django import forms


class DateInput(forms.DateTimeInput):
    input_type="date"
    
class EventForm(ModelForm):
    class Meta:
        model=Event
        fields="__all__"
        exclude=('nbr_participant','state','participants','organisateur')
        
        widgets={'evt_date':DateInput()}