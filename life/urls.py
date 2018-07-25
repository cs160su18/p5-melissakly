from django.urls import path
from . import views

urlpatterns = [
  path('', views.index, name='index'),
  path('spendings/', views.spend, name='spend'),
  path('earnings/', views.earn, name='earn'),
  path('goals/', views.goals, name='goals'),
]