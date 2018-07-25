from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.validators import ASCIIUsernameValidator
from django.contrib.auth.models import User
import datetime

class Achievement(models.Model):
  goal = models.DecimalField(max_digits=6, decimal_places=2)
  week = models.DateTimeField(null=True, blank=True)
  achieved = models.BooleanField(default=False)
  def __str__(self):
    return self.name

class Earning(models.Model):
  name = models.CharField(max_length=50)
  amount = models.DecimalField(max_digits=6, decimal_places=2)
  description = models.CharField(max_length=100)
  def __str__(self):
    return self.name
      
class Spending(models.Model):
  name = models.CharField(max_length=50)
  cost = models.DecimalField(max_digits=6, decimal_places=2)
  description = models.CharField(max_length=100)
  def __str__(self):
    return self.name