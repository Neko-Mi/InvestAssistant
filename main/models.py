import datetime
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
from InvestAssistant import settings
# from InvestAssistant import settings


class Question(models.Model):
    title = models.CharField(max_length=400)
    visible = models.BooleanField(default=False)
    max_points = models.FloatField()

    def __str__(self):
           return self.title

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    title = models.CharField(max_length=400)
    points = models.FloatField()
    lock_other = models.BooleanField(default=False)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.title

# class Answer(models.Model):
#     user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING)
#     question = models.ForeignKey(Question, on_delete=models.DO_NOTHING)
#     choice = models.ForeignKey(Choice, on_delete=models.DO_NOTHING)
#     created = models.DateTimeField(auto_now_add=True)
#
#     def __str__(self):
#         return self.choice.title

class User(AbstractUser):
    answers = models.CharField(max_length=400, default='low')
    money = models.CharField(max_length=400, default='low')
    risk = models.CharField(max_length=400, default='low')
    time_invest = models.CharField(max_length=400, default='low')


class Answer(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    choice = models.ForeignKey(Choice, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    def __str__(self):
        return self.choice.title


class Stock(models.Model):
    name = models.CharField(max_length=200)
    code = models.CharField(max_length=20)
    mape = models.FloatField(default=0)
    price = models.FloatField(default=0)
    price_predict = models.FloatField(default=0)
    price_predict_3 = models.FloatField(default=0)
    price_predict_6 = models.FloatField(default=0)
    rec_day_new = models.DateField(default='2020-01-01')
    reg_day_future = models.DateField(default='2020-01-01')

    def __str__(self):
        return self.name

    def __float__(self):
        return self.mape