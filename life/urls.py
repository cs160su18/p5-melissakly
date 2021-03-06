from django.urls import path
from . import views

urlpatterns = [
  path('', views.index, name='index'),
  path('spendings/', views.spend, name='spend'),
  path('earnings/', views.earn, name='earn'),
  path('goals/', views.goals, name='goals'),
  path('view_earnings/', views.earningsList, name='earnings'),
  path('view_spendings/', views.spendingsList, name='spendings'),
  path('view_goals/', views.goalsList, name='all-goals'),
#   path('view_earnings/<int:pk>', views.EarnListDetailView.as_view(), name='earnings-detail')
]