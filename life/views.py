from django.shortcuts import render, HttpResponse
from django.core import serializers
from django.urls import reverse
from django.views import generic
from django import forms
from .forms import *
from life.models import *

def spend(request):
    if request.method == 'POST':
        form = SpendForm(request.POST)
        if form.is_valid():
            spending = Spending.create(form.cleaned_data['name'], form.cleaned_data['cost'], form.cleaned_data['description'])
            spending.save()
    else:
        form = SpendForm()
    return render(request, 'life/spendings.html', {'form': form})

def earn(request):
    if request.method == 'POST':
        form = EarnForm(request.POST)
        if form.is_valid():
            earning = Earning.create(form.cleaned_data['name'], form.cleaned_data['amount'], form.cleaned_data['description'])
            earning.save()
    else:
        form = EarnForm()
    return render(request, 'life/earnings.html', {'form': form}) 

  
def goals(request):
    if request.method == 'POST':
        form = GoalsForm(request.POST)
        if form.is_valid():
            goal = Achievement.create(form.cleaned_data['goal'], form.cleaned_data['week'], form.cleaned_data['achieved'])
            goal.save()
    else:
        form = GoalsForm()

    return render(request, 'life/goals.html', {'form': form})  


def index(request):
    return render(request, 'life/index.html')
  
def spendingsList(request):
  if request.method == "GET":
    all_groups = Spending.objects.all()
  return render(request, 'life/view_spendings.html', {'spend_list': all_groups}) 

def goalsList(request):
  if request.method == "GET":
    all_groups = Achievement.objects.all()
  return render(request, 'life/view_goals.html', {'goals_list': all_groups}) 

def earningsList(request):
  if request.method == "GET":
    all_groups = Earning.objects.all()
  return render(request, 'life/view_earnings.html', {'earnings': all_groups})   
  
# class EarnListView(generic.ListView):
#     model = Earning
#     def get_context_data(self, **kwargs):
#         # Call the base implementation first to get the context
#         context = super(EarnListView, self).get_context_data(**kwargs)
#         # Create any data and add it to the context
#         context['some_data'] = 'This is just some data'
#         return context
      
      
# class EarnListDetailView(generic.DetailView):
#     model = Earning
#     def get_context_data(self, **kwargs):
#         context = super(EarnListDetailView, self).get_context_data(**kwargs)
#         context['earn'] = self.object.deals.all()     
#         item = context['earn'].name
#         items = []
#         all_groups = Groups.objects.all()
#         for obj in all_groups:
#             items.append(obj.name)
#         response = serialize('json', all_groups)
#         return HttpResponse(response, content_type="application/json")
#         if item in items:
#             context['addable'] = False
#         else:
#             context['addable'] = True
#         return context
      
      
      
      
#   handles a get request
def groups(request):
  if request.method == 'POST':
    print('Hello!')
    return HttpResponse('')
  else:
    all_groups = Groups.objects.all()
    response = serialize('json', all_groups)
    return HttpResponse(response, content_type="application/json")
