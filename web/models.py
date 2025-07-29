import datetime
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Expense (models.Model):
    text = models.CharField(max_length=256)
    expenseDate = models.DateTimeField()
    amount = models.BigIntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__ (self):
        
        return f"{self.amount} - {dateformater(self.expenseDate)}"

class Income (models.Model):
    text = models.CharField(max_length=256)
    incomeDate = models.DateTimeField()
    amount = models.BigIntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__ (self):
        return f"{self.amount} - {dateformater(self.incomeDate)}"


def dateformater(date):
    date_string = str(date)
    datetime_object = datetime.datetime.strptime(date_string, "%Y-%m-%d %H:%M:%S%z")
    formatted_datetime_str = datetime_object.strftime("%Y/%m/%d %H:%M")
    return formatted_datetime_str