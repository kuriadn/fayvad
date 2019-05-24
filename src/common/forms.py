from __future__ import unicode_literals
from django import forms
from .models import *

def getExpenses():
  expenses = ExpenseType.objects.all().order_by('exp')
  exps = []
  for expense in expenses:
   exps.append((str(expense), expense))
  expenses = tuple(exps)
  return expenses

EXPENSES = getExpenses()

class PositionForm(forms.ModelForm):
  class Meta:
    model = Position
    fields = ('post',)

class StaffForm(forms.ModelForm):
  class Meta:
  	model = Staff 
  	fields = ('idno', 'fname', 'lname', 'post', 'address', 'telno', 'email')

class PayModeForm(forms.ModelForm):
  class Meta:
  	model = PayMode 
  	fields = ('mode',)

class ExpenseTypeForm(forms.ModelForm):
  class Meta:
  	model = ExpenseType 
  	fields = ('exp',)

class DriverForm(forms.ModelForm):
  class Meta:
  	model = Driver 
  	fields = ('idno', 'fname', 'lname', 'post', 'dlno', 'duelicense', 'address', 'telno', 'email')

class VehicleForm(forms.ModelForm):
  class Meta:
    model = Vehicle 
    fields = ('regno', 'dueinsurance')

class ExpenseForm(forms.ModelForm):
  class Meta:
    model = Expense 
    fields = ('exptype', 'amount', 'date', 'vehicle', 'desc')    

class TripForm(forms.ModelForm):
  class Meta:
  	model = Trip 
  	fields = ('van', 'amount', 'datepaid', 'desc')

class PickPeriodForm(forms.Form):
  from django.forms.widgets import SelectDateWidget
  from transport.forms import SELECTYEARS
  start = forms.DateField(widget=SelectDateWidget(years=SELECTYEARS), initial=timezone.now)
  end = forms.DateField(widget=SelectDateWidget(years=SELECTYEARS), initial=timezone.now)

class PickExpPeriodForm(forms.Form):
  from django.forms.widgets import SelectDateWidget
  from transport.forms import SELECTYEARS
  expense = forms.CharField(max_length=30, required=True, widget=forms.Select(choices=EXPENSES))
  start_date = forms.DateField(widget=SelectDateWidget(years=SELECTYEARS), initial=timezone.now)
  end_date = forms.DateField(widget=SelectDateWidget(years=SELECTYEARS), initial=timezone.now)

