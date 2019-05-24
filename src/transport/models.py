from django.db import models
from django.utils import timezone 
from common.models import *

class Term(models.Model):
  first = 'First'
  second = 'Second'
  third = 'Third'
  CHOICES = ((first,'First'), (second,'Second'), (third, 'Third'),)
  term = models.CharField(max_length=10, choices=CHOICES)
  year = models.IntegerField(default=2015, verbose_name='Year')
  
  class Meta:
    unique_together = ('term', 'year')
    ordering = ['year', 'term']

  def __str__(self):
    return self.term + ' Term ' + str(self.year)

  # def get_absolute_url(self):
  #   return reverse('term_list', kwargs={'pk': self.pk})

class Parent(models.Model):
  pname = models.CharField(max_length=50, primary_key=True, verbose_name='Parent Name')
  phone = models.CharField(max_length=10)

  class Meta:
    ordering = ['pname']

  def __str__(self):
    return self.pname

class Zone(models.Model):
  zone = models.CharField(max_length=5, primary_key=True)

  class Meta:
    ordering = ['zone']

  def __str__(self):
    return self.zone 

class Rate(models.Model):
  zone = models.ForeignKey(Zone, on_delete=models.CASCADE)
  rate = models.DecimalField(max_digits=10, decimal_places=2)
  term = models.ForeignKey(Term, on_delete=models.CASCADE)

  class Meta:
    unique_together = ('zone', 'term')
    ordering = ['zone']

  def __str__(self):
    return '{0} - {1}'.format(self.zone.zone, self.term.term)  

class Estate(models.Model):
  estate = models.CharField(max_length=50, primary_key=True)
  zone = models.ForeignKey(Zone, on_delete=models.CASCADE)

  class Meta:
    ordering = ['estate']

  def __str__(self):
    return self.estate

class Pupil(models.Model):
  fname = models.CharField(max_length=50, verbose_name='First Name')
  sname = models.CharField(max_length=50, verbose_name='Surname')
  parent = models.ForeignKey(Parent, on_delete=models.CASCADE)

  class Meta:
    ordering = ['fname']
    unique_together = ['fname', 'sname', 'parent']

  def __str__(self):
    return self.fname + " " + self.sname

class EstatePupil(models.Model):
  pupil = models.ForeignKey(Pupil, on_delete=models.CASCADE)
  estate = models.ForeignKey(Estate, on_delete=models.CASCADE)

  class Meta:
    unique_together = ('pupil', 'estate')
    ordering = ['estate']

  def __str__(self):
    return self.pupil.fname + ': ' + self.estate.estate

class TermPupil(models.Model):
  pupil = models.ForeignKey(Pupil, on_delete=models.CASCADE)
  term = models.ForeignKey(Term, on_delete=models.CASCADE)
 
  class Meta:
    unique_together = ('pupil', 'term')
    ordering = ['term', 'pupil']

  def __str__(self):
    return self.pupil.fname + ': ' + str(self.term.term) + ' ' + str(self.term.year) 

class Payment(ModelPayment):
  pupil = models.ForeignKey(Pupil, on_delete=models.CASCADE)
  
  class Meta:
    unique_together = ('pupil', 'datepaid', 'amount')
    ordering = ['datepaid', 'pupil']

  def __str__(self):
    pname = str(self.pupil.fname + " " + self.pupil.sname)
    return pname + " - " + str(self.datepaid)

