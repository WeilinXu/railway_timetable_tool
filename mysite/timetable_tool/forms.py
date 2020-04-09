
from django import forms
from timetable_tool.models import tickets_sold
from django.core.files.uploadedfile import InMemoryUploadedFile

from django import forms
from django.core.exceptions import ValidationError
from django.core import validators

class CreateForm(forms.ModelForm):
    class Meta:
        model = tickets_sold
        fields = ['quantity']  # Picture is manual

class RouteForm(forms.Form):
    route_input = forms.CharField(label='Route No.', max_length=30)
    date_input = forms.CharField(label='Date', widget=forms.widgets.DateTimeInput(attrs={"type": "date"})) 

class StationForm(forms.Form):
    station_input = forms.CharField(label='Station', max_length=30)
    date_input = forms.CharField(label='Date', widget=forms.widgets.DateTimeInput(attrs={"type": "date"})) 

class TrainForm(forms.Form):
    depart_input = forms.CharField(label='Depart From', max_length=30)
    dest_input = forms.CharField(label='Go To', max_length=30)
    date_input = forms.CharField(label='Date', widget=forms.widgets.DateTimeInput(attrs={"type": "date"})) 