from django.db import models
from django.utils import timezone 
from django.core.validators import *
from common.models import *

class Class(BaseClass):
  description = models.CharField(max_length=100)
  system = models.CharField(max_length=10, default='Old')

  class Meta:
    ordering = ['system', 'cls']

class Tutor(models.Model):
  instructor = models.ForeignKey(Driver, on_delete=models.CASCADE, verbose_name='Instructor')
  insLic = models.CharField(max_length=10, verbose_name='Instructor Licence No.')

  class Meta:
    ordering = ['instructor']

  def __str__(self):
    return self.instructor.fname + ' ' + self.instructor.lname 

class Student(Person):
  cls = models.ForeignKey(Class, on_delete=models.CASCADE, verbose_name='Class')

  class Meta:
    ordering = ['fname', 'lname']

class Branch(models.Model):
  bname=models.CharField(max_length=15, verbose_name='Name')

  class Meta:
    ordering=['bname']

  def __str__(self):
    return self.bname

class StudentEnrolment(models.Model):
  student = models.ForeignKey(Student, on_delete=models.CASCADE)
  branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
  date_enrol = models.DateField(default=timezone.now, verbose_name='Date Enrolled')

  class Meta:
    unique_together=['student', 'branch']
    ordering=['branch', 'student']

  def __str__(self):
    return self.student.fname + ' ' + self.student.lname + ' - ' + self.branch.bname

class ExamBooking(models.Model):
  student = models.ForeignKey(Student, on_delete=models.CASCADE)
  pdl =  models.CharField(max_length=11, 
    validators=[RegexValidator(regex=r'^PDL-[ABEFRPT]{3}[0-9]{4}$')], 
    verbose_name='Provisional Driving License')
  date = models.DateField(default=timezone.now)
  venue = models.CharField(max_length=20, verbose_name='Exam Venue', default='Ruaraka')

  class Meta:
    unique_together = ('student', 'date')
    ordering = ['student']

  def __str__(self):
    return self.student.fname + ' ' + self.student.lname

class Period(models.Model):
  start = models.DateField(default=timezone.now)
  stop = models.DateField(default=timezone.now)
 
  class Meta:
    unique_together = ('start', 'stop')
    ordering = ['start', 'stop']

  def __str__(self):
    return str(self.start) + ' - ' + str(self.stop)

class Rate(models.Model):
  clss = models.ForeignKey(Class, on_delete=models.CASCADE, verbose_name='Class')
  rate = models.DecimalField(decimal_places=2, max_digits=10)
  period = models.ForeignKey(Period, on_delete=models.CASCADE)

  class Meta:
    unique_together = ('clss', 'rate', 'period')
    ordering = ['clss', 'period']

class Attendance(models.Model):
  practical = 'Practical Class'
  theory = 'Theory Class'
  CLASSES = ((practical, practical), (theory, theory),)
  student = models.ForeignKey(Student, on_delete=models.CASCADE)
  lesson = models.IntegerField(default=1)
  typ = models.CharField(max_length=50, choices=CLASSES, verbose_name='Type of Lesson', default=theory)
  date = models.DateField(default=timezone.now)
  instructor = models.ForeignKey(Tutor, on_delete=models.CASCADE)

  class Meta:
    unique_together = ('student', 'lesson', 'date', 'instructor')
    ordering = ['student', 'lesson']

  def __str__(self):
    return self.student.fname + ' ' + self.student.lname + ' - Lesson ' + str(self.lesson)

class Payment(ModelPayment):
  student = models.ForeignKey(Student, on_delete=models.CASCADE)

  class Meta:
    unique_together = ('student', 'datepaid', 'amount')
    ordering = ['student']

  def __str__(self):
    return self.student.fname + ' ' + self.student.lname + ': ' + str(self.amount) 

class License(models.Model):
  pdl = 'Provisional Driving License'
  idl = 'Interim Driving License'
  fdl = 'Driving License'
  CHOICES = ((pdl, pdl), (idl, idl), (fdl, fdl),)
  student = models.ForeignKey(Student, on_delete=models.CASCADE)
  dl_type = models.CharField(max_length=50, choices=CHOICES, verbose_name='Type of Driving License', default=pdl)
  dl = models.CharField(max_length=10, verbose_name='Driving License No.', primary_key=True)
  dateissued = models.DateField(default=timezone.now, verbose_name='Date Issued')

  class Meta:
    unique_together = ('student', 'dl', 'dateissued')
    ordering = ['student']

  def __str__(self):
   return self.student.fname + ' ' + self.student.lname + ': ' + self.dl

class Discharge(models.Model):
  student = models.ForeignKey(Student, on_delete=models.CASCADE)
  dl = models.CharField(max_length=10, verbose_name='Driving License No.')
  collected = models.DateField(default=timezone.now)
  collector = models.CharField(max_length=50, verbose_name='Collected By?')

  class Meta:
    unique_together = ('student', 'dl', 'collected', 'collector')
    ordering = ['student']

  def __str__(self):
    return self.student.fname + ' ' + self.student.lname + ': ' + self.dl
