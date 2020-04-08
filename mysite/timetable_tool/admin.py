
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from timetable_tool.models import stations, train_records, stop_records, tickets, tickets_sold

# Register your models here.

admin.site.register(stations)
admin.site.register(train_records)
admin.site.register(stop_records)
admin.site.register(tickets)
admin.site.register(tickets_sold)
'''
# Define an inline admin descriptor for customer model
# which acts a bit like a singleton
class customerInline(admin.StackedInline):
    model = customers
    can_delete = False
    verbose_name_plural = 'customer'

# Define a new User admin
class UserAdmin(BaseUserAdmin):
    inlines = (customerInline,)

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
'''