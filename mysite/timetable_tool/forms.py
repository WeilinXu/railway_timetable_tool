
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
