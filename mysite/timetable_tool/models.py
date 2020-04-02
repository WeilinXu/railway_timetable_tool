from django.db import models
from django.core.validators import MinLengthValidator

# TODO: leave primary key as default now
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