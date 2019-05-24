from __future__ import unicode_literals
from django import forms
from django.forms.widgets import SelectDateWidget
import calendar, datetime
from django.utils import timezone 
from .models import *

TYPE = (('parent', 'Parent'), ('estate', 'Estate'),)
TERMS = (('first', 'First'), ('second', 'Second'), ('third', 'Third'),)

def getYears():
  styr = 2015
  rng = datetime.datetime.now().year - styr + 2
  yrs = []
  for i in range(rng + 1):
    yrs.append(styr + i)
  yrs = tuple(yrs)
  return yrs

SELECTYEARS = getYears()

def getCurrentYear():
  return timezone.now().year

def getCurrentMonth():
  return timezone.now().month

def getCurrentDay():
  return timezone.now().day 

def getPupils():
  pupils = Pupil.objects.all().order_by('parent')
  pups = []
  for pupil in pupils:
    pups.append((str(pupil), pupil))
  pupils = tuple(pups)
  return pupils

PUPILS = getPupils()

def getParents():
  parents = Parent.objects.all().order_by('pname')
  pars = []
  for parent in parents:
    pars.append((str(parent), parent))
  parents = tuple(pars)
  return parents

PARENTS = getParents()

class TermForm(forms.ModelForm):
  class Meta:
    model = Term
    fields = ('term', 'year')

class ParentForm(forms.ModelForm):
  class Meta:
    model = Parent 
    fields = ('pname', 'phone')

class RateForm(forms.ModelForm):
  class Meta:
  	model = Rate 
  	fields = ('zone', 'rate', 'term')

class ZoneForm(forms.ModelForm):
  class Meta:
    model = Zone
    fields = ('zone',)

# class ClassForm(forms.ModelForm):
#   class Meta:
#   	model = Class 
#   	fields = ('cls',)

class EstateForm(forms.ModelForm):
  class Meta:
  	model = Estate 
  	fields = ('estate', 'zone')

class PupilForm(forms.ModelForm):
  class Meta:
  	model = Pupil 
  	fields = ('fname', 'sname', 'parent')

class EstatePupilForm(forms.ModelForm):
  class Meta:
  	model = EstatePupil 
  	fields = ('pupil', 'estate')

class TermPupilForm(forms.ModelForm):
  class Meta:
    model = TermPupil
    fields = ('pupil', 'term')

class PaymentForm(forms.ModelForm):
  class Meta:
  	model = Payment 
  	fields = ('pupil', 'amount', 'datepaid', 'mode')

class PickPeriodForm(forms.Form):
  start = forms.DateField(widget=SelectDateWidget(years=SELECTYEARS), initial=timezone.now)
  end = forms.DateField(widget=SelectDateWidget(years=SELECTYEARS), initial=timezone.now)

class PickTermForm(forms.Form):
  term = forms.CharField(max_length=10, required=True, widget=forms.Select(choices=TERMS))
  year = forms.IntegerField(min_value=2015, max_value=2020, initial=getCurrentYear)

class PickMonthYearForm(forms.Form):
  months=[]
  for i in range(13):
    month = calendar.month_name[i]
    months.append((month.lower(), month.title()))
  MONTHS=tuple(months[1:])
  month = forms.CharField(max_length=15, required=True, widget=forms.Select(choices=MONTHS), initial=getCurrentMonth)
  year = forms.IntegerField(min_value=SELECTYEARS[0], max_value=SELECTYEARS[len(SELECTYEARS)-1], initial=getCurrentYear)
  
class PickSummaryForm(forms.Form):
  sumtype = forms.CharField(max_length=10, required=True, widget=forms.Select(choices=TYPE))
  term = forms.CharField(max_length=10, required=True, widget=forms.Select(choices=TERMS))
  year = forms.IntegerField(min_value=SELECTYEARS[0], max_value=SELECTYEARS[len(SELECTYEARS)-1], initial=getCurrentYear)

class PickPupilForm(forms.Form):
  pupils = forms.CharField(max_length=100, required=True, widget=forms.Select(choices=PUPILS))

class PickParentForm(forms.Form):
  parent = forms.CharField(max_length=100, required=True, widget=forms.Select(choices=PARENTS))