
from django import forms
from timetable_tool.models import tickets_sold
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.conf import settings

from django import forms
from django.core.exceptions import ValidationError
from django.core import validators

from django.utils.translation import ugettext_lazy as _

class RouteForm(forms.Form):
    route_input = forms.CharField(label=_('Route No.'), max_length= settings.MAX_ROUTE_LENGTH, \
                    widget=forms.TextInput(attrs={'id': 'id_route_input'}))
    date_input = forms.CharField(label=_('Date'), widget=forms.widgets.DateTimeInput(attrs={"type": "date"})) 

class StationForm(forms.Form):
    station_input = forms.CharField(label=_('Station'), max_length = settings.MAX_STATION_LENGTH, \
                        widget=forms.TextInput(attrs={'id': 'id_station_input'}))
    date_input = forms.CharField(label=_('Date'), widget=forms.widgets.DateTimeInput(attrs={"type": "date"})) 

class TrainForm(forms.Form):
    depart_input = forms.CharField(label=_('Depart From'), max_length = settings.MAX_STATION_LENGTH, \
                        widget=forms.TextInput(attrs={'id': 'id_station_input2'}))
    dest_input = forms.CharField(label=_('Go To'), max_length = settings.MAX_STATION_LENGTH, \
                        widget=forms.TextInput(attrs={'id': 'id_station_input'}))
    date_input = forms.CharField(label=_('Date'), widget=forms.widgets.DateTimeInput(attrs={"type": "date"})) 