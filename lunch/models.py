from django.db import models

# Create your models here.


class LunchMenu(models.Model):
    dish_name = models.CharField(max_length=255)

    class Meta:
        db_table = 'LunchMenu'

    def __str__(self):
        return self.dish_name


class Admin(models.Model):
    friday_lunch_iterator = models.IntegerField()
    weekday_lunch_iterator = models.IntegerField()
    lunch_time = models.TimeField(default="15:00:00")  # Assuming default lunch time

    class Meta:
        db_table = 'admin'

    def __str__(self):
        return f'FridayIterator: {self.friday_lunch_iterator}, WeekdayIterator: {self.weekday_lunch_iterator}, LunchTime: {self.lunch_time}'
