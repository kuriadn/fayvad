from __future__ import unicode_literals
from django import forms
from .models import *

def getTenants():
  tenants = Tenant.objects.all().order_by('name')
  tens = []
  for tenant in tenants:
    tens.append((str(tenant), tenant))
  tenants = tuple(tens)
  return tenants

TENANTS = getTenants()

class TenantForm(forms.ModelForm):
  class Meta:
    model = Tenant
    fields = ('name', 'phone')

class RoomForm(forms.ModelForm):
  class Meta:
  	model = Room 
  	fields = ('site', 'room',)

class RentRegimeForm(forms.ModelForm):
  class Meta:
  	model = Rent_Regime  
  	fields = ('site', 'amount', 'beg_date', 'end_date')

class Room_TenantForm(forms.ModelForm):
  class Meta:
  	model = Room_Tenant  
  	fields = ('tenant', 'room', 'commencement')

class PaymentForm(forms.ModelForm):
  class Meta:
  	model = Payment 
  	fields = ('tenant', 'amount', 'datepaid', 'mode')

class PickTenantForm(forms.Form):
  tenants = forms.CharField(max_length=100, required=True, widget=forms.Select(choices=TENANTS))
