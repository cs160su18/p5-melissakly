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
  
  def create(cls, goal, week, achieved):
        item1 = cls(name=name, amount=amount, achieved=achieved)
        return item1

class Earning(models.Model):
  name = models.CharField(max_length=50)
  amount = models.DecimalField(max_digits=6, decimal_places=2)
  description = models.CharField(max_length=100)
  def __str__(self):
    return self.name
  
  def create(cls, name, amount, description):
        item1 = cls(name=name, amount=amount, description=description)
        return item1
      
class Spending(models.Model):
  name = models.CharField(max_length=50)
  cost = models.DecimalField(max_digits=6, decimal_places=2)
  description = models.CharField(max_length=100)
  def __str__(self):
    return self.name
  
  def create(cls, name, cost, description):
        item1 = cls(name=name, cost=cost, description=description)
        return item1

# user = User.objects.create_user('User1', 'user1@user1.user1', 'password')
# user.save()