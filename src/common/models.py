from django.db import models
from django.utils import timezone 
from profiles.models import *

class Person(models.Model):
  idno = models.CharField(max_length=10, primary_key=True, verbose_name='ID. No.')
  fname = models.CharField(max_length=20, verbose_name='First Name', default='')
  lname = models.CharField(max_length=20, verbose_name='Last Name', default='')
  address = models.CharField(max_length=100, null=True, blank=True)
  telno = models.CharField(max_length=10, verbose_name='Phone No.', default='')
  email = models.EmailField(null=True, blank=True)

  class Meta:
  	abstract = True

  def __str__(self):
  	return self.fname + ' ' + self.lname

class Position(models.Model):
  post = models.CharField(max_length=50, primary_key=True, verbose_name='Position', default='Office Administrator')

  def __str__(self):
  	return self.post
 
class BaseStaff(Person):
  post = models.ForeignKey(Position, on_delete=models.CASCADE, verbose_name='Position')
  
  class Meta:
  	abstract = True

class Staff(BaseStaff):
  pass

class BaseClass(models.Model):
  cls = models.CharField(max_length=50, primary_key=True, verbose_name='Class')

  def __str__(self):
    return self.cls

  class Meta:
    abstract = True
    verbose_name = "class"
    verbose_name_plural = "classes"

class PayMode(models.Model):
  mode = models.CharField(max_length=10)

  class Meta:
    ordering=['mode']

  def __str__(self):
    return self.mode 

class ExpenseType(models.Model):
  exp = models.CharField(max_length=20, verbose_name='Expense Type')

  class Meta:
    ordering=['exp']

  def __str__(self):
    return self.exp

class Driver(BaseStaff):
  dlno = models.CharField(max_length=10, verbose_name='Driving Licence No.', default='1')
  duelicense = models.DateField(default=timezone.now, verbose_name="Driving License Expiry Date")

class Vehicle(models.Model):
  regno = models.CharField(max_length=8, primary_key=True, verbose_name="Reg. No.")
  dueinsurance = models.DateField(default=timezone.now, verbose_name="Insurance Due Date")

  class Meta:
    ordering=['regno']

  def __str__(self):
    return self.regno

class ModelPayment(models.Model):
  datepaid = models.DateField(verbose_name='Date Paid', default=timezone.now)
  amount = models.DecimalField(max_digits=10, decimal_places=2)
  mode = models.ForeignKey(PayMode, related_name='%(app_label)s_%(class)s_mode', on_delete=models.CASCADE)
  
  class Meta:
    abstract = True
    ordering = ['datepaid']

class Expense(models.Model):
  exptype = models.ForeignKey(ExpenseType, on_delete=models.CASCADE, verbose_name='Expense Type')
  amount = models.DecimalField(max_digits=10, decimal_places=2)
  vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE, blank=True, null=True)
  date = models.DateField(default=timezone.now)
  desc = models.TextField(max_length=300, verbose_name='Description')

  class Meta:
    unique_together = ('exptype', 'amount', 'date', 'vehicle')
    ordering=['date']

  def __str__(self):
    return self.exptype.exp + ' ' + str(self.date)

class Trip(models.Model):
  van = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
  amount = models.DecimalField(max_digits=10, decimal_places=2)
  datepaid = models.DateField(default=timezone.now)
  desc = models.TextField(max_length=300, verbose_name='Description')

  class Meta:
    ordering = ['datepaid']

  def __str__(self):
    return self.van.regno.upper() + '-' + str(self.date)
