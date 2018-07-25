from django.urls import path
from . import views

urlpatterns = [
  path('', views.index, name='index'),
  path('groups/',views.groups, name='groups'),
  path('life/spendings/', views.spend, name='spending'),
  path('life/earnings/', views.earn, name='earning'),
  path('life/goals/', views.goals, name='goals'),
]