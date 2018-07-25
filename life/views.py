from django.shortcuts import render, HttpResponse
from django.core import serializers
from django.urls import reverse
from django.views import generic
from django import forms
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
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
  
  
# def goals(request):
#     if request.method == 'POST':
#         form = StepsForm(request.POST)
#         if form.is_valid():
#             curTitle = form.cleaned_data['title']
#             curDate = form.cleaned_data['date']
#             curGoal = form.cleaned_data['goal']
#             curAchieved = form.cleaned_data['achieved']
#             newSteps.save()
       
    
#     form = StepsForm()
#     return render(request, 'life/steps.html', {'form' : form})

# def goal(request):
#     curTitle = ""
#     print("going through goals")
#     if request.method == 'POST':
#         form = SearchForm(request.POST)
#         print("entered goals post request")
#         if form.is_valid():
#             print("form is valid")
#             curTitle = form.cleaned_data['title']
#             print("the title is: " + curTitle)
#             # render the proper page    
#             curSpend = None
#     form = SearchForm()
#     context =  { 
#       'title' : curTitle,
#       'form' : form,
#     }
#     print("The context" + str(context))
#     return render(request, 'life/earnings.html', context)


# def spend(request):
#     curTitle = ""
#     print("going through spendings")
#     if request.method == 'POST':
#         form = SearchForm(request.POST)
#         print("entered spend post request")
#         if form.is_valid():
#             print("form is valid")
#             curTitle = form.cleaned_data['title']
#             print("the title is: " + curTitle)
#             # render the proper page    
#             curSpend = None
#     form = SearchForm()
#     context =  { 
#       'title' : curTitle,
#       'form' : form,
#     }
#     print("The context" + str(context))
#     return render(request, 'life/spendings.html', context)


def index(request):
    return render(request, 'life/index.html')
  
  
# def earn(request):
#     curTitle = ""
#     print("going through earn")
#     if request.method == 'POST':
#         form = SearchForm(request.POST)
#         print("entered earn post request")
#         if form.is_valid():
#             print("form is valid")
#             curTitle = form.cleaned_data['title']
#             print("the title is: " + curTitle)
#             # render the proper page    
#             curSpend = None
#     form = SearchForm()
#     context =  { 
#       'title' : curTitle,
#       'form' : form,
#     }
#     print("The context" + str(context))
#     return render(request, 'life/earnings.html', context)  

  
  
  #   handles a get request
def groups(request):
  if request.method == 'POST':
    print('Hello!')
    return HttpResponse('')
  else:
    all_groups = Groups.objects.all()
    response = serialize('json', all_groups)
    return HttpResponse(response, content_type="application/json")

