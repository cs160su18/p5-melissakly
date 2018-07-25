from django import forms

from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

class GoalsForm(forms.Form):
    goal = forms.CharField(label="Enter your goal for the week.", max_length=50)
    week = forms.DecimalField(label="Enter the date.")
    achieved = forms.BooleanField(label="Enter the whether you achieved your goal.")


class EarnForm(forms.Form):
    name = forms.CharField(label="Enter the item's name.", max_length=50)
    amount = forms.DecimalField(label="Enter amount earned.")
    description = forms.CharField(label="Enter the description of earnings.", max_length=100)


class SpendForm(forms.Form):
    name = forms.CharField(label="Enter the item's name.", max_length=50)
    cost = forms.DecimalField(label="Enter the item's price.")
    description = forms.CharField(label="Enter the description of spendings.", max_length=100)
    