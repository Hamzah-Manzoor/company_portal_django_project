from django.db import models
from django.utils import timezone

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
        db_table = 'Admin'

    def __str__(self):
        return f'FridayIterator: {self.friday_lunch_iterator}, WeekdayIterator: {self.weekday_lunch_iterator}, LunchTime: {self.lunch_time}'


class LunchReview(models.Model):
    date = models.DateField(default=timezone.now)
    lunch_menu = models.ForeignKey(LunchMenu, on_delete=models.CASCADE)
    likes = models.JSONField(default=list, blank=True)
    dislikes = models.JSONField(default=list, blank=True)

    class Meta:
        db_table = 'LunchReview'

    def __str__(self):
        return f'Date: {self.date}, Menu: {self.lunch_menu}, Likes: {len(self.likes)}, Dislikes: {len(self.dislikes)}'
