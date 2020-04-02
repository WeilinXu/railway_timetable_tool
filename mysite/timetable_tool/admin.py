
from django.contrib import admin
from timetable_tool.models import stations, train_records, stop_records

# Register your models here.

admin.site.register(stations)
admin.site.register(train_records)
admin.site.register(stop_records)