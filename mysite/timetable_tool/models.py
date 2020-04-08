from django.db import models
from django.core.validators import MinLengthValidator
from django.contrib.auth.models import User
from django.conf import settings


# leave primary key as default now
class stations(models.Model):   # actual name: timetable_tool_stations
    station_name = models.CharField(
            max_length=20,
            validators=[MinLengthValidator(2, "Station Name must be greater than 1 character")]
    )

    def __str__(self):
        return self.station_name

class train_records(models.Model):  # actual name: timetable_tool_train_records
    train_number = models.CharField(
            max_length=20,
            validators=[MinLengthValidator(2, "Train Number must be greater than 1 character")]
    )
    train_from = models.ForeignKey(stations, related_name='from_id', on_delete=models.CASCADE)  # train_from_id
    train_to = models.ForeignKey(stations, related_name='to_id', on_delete=models.CASCADE)  # train_to_id
    def __str__(self):
        return self.train_number

class stop_records(models.Model):   # actual name: timetable_tool_stop_records
    class Meta:
        unique_together = (('train_record_id', 'station_id'),)
    train_record = models.ForeignKey(train_records, on_delete=models.CASCADE)
    station = models.ForeignKey(stations, on_delete=models.CASCADE) # station_id
    station_no = models.PositiveSmallIntegerField()
    
    arr_time = models.TimeField()
    arr_day = models.PositiveSmallIntegerField()
    dep_time = models.TimeField()
    dep_day = models.PositiveSmallIntegerField()

    # dist = models.PositiveSmallIntegerField(blank=True, default=None)

class tickets(models.Model):
    class Meta:
        unique_together = (('stop_from_id', 'stop_to_id', 'train_date'),)
    stop_from = models.ForeignKey(stop_records, related_name="sr1", on_delete=models.CASCADE)
    stop_to = models.ForeignKey(stop_records, related_name="sr2", on_delete=models.CASCADE)
    train_date = models.DateField()
    tickets_avaliable = models.PositiveSmallIntegerField()

'''
# TODO: allow one customer to buy tickets for others
class customers(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # name = models.CharField(max_length=100)
'''

class tickets_sold(models.Model):
    class Meta:
        unique_together = (('ticket_id', 'customer_id'),)
    ticket = models.ForeignKey(tickets, on_delete=models.CASCADE)
    customer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    seat_number = models.PositiveSmallIntegerField()
    quantity = models.PositiveSmallIntegerField(default=1)


