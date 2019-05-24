from django.db import models
from common.models import *
from django.utils import timezone

class Tenant(models.Model):
  name = models.CharField(max_length=50, verbose_name='Tenant Name')
  phone = models.CharField(max_length=10, verbose_name='Mobile Phone')

  class Meta:
    unique_together=('name', 'phone')
    ordering = ['name']

  def __str__(self):
  	return self.name

class Room(models.Model):
  site = models.CharField(max_length=10, verbose_name='Site', default='Ruiru')
  room = models.CharField(max_length=5, verbose_name='Room')

  class Meta:
    ordering = ['site', 'room']

  def __str__(self):
  	return self.room 

class Rent_Regime(models.Model):
  site = models.CharField(max_length=10, verbose_name='Site', default='Ruiru')
  amount = models.DecimalField(max_digits=10, decimal_places=2)
  beg_date = models.DateField(verbose_name='Beginning Date', default=timezone.now)
  end_date = models.DateField(verbose_name='Ending Date', default=timezone.now)

  class Meta:
    unique_together=('site', 'amount', 'beg_date')
    ordering = ['site', 'end_date']

  def __str__(self):
  	return str(self.amount) + ' for ' + str(self.beg_date) + ' - ' + str(self.end_date)

class Room_Tenant(models.Model):
  tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE)
  room = models.ForeignKey(Room, on_delete=models.CASCADE)
  commencement = models.DateField(verbose_name='Date Commenced Occupation', default=timezone.now)

  class Meta:
    unique_together=('tenant', 'room')
    ordering = ['room']

  def __str__(self):
  	return self.tenant.name + ' in ' + self.room.room

class Payment(ModelPayment):
  tenant= models.ForeignKey(Tenant, on_delete=models.CASCADE)
  
  class Meta:
    unique_together = ('tenant', 'datepaid', 'amount')
    ordering = ['datepaid', 'tenant']

  def __str__(self):
    pname = str(self.tenant.name )
    return pname + " - " + str(self.datepaid)
