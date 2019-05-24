from __future__ import unicode_literals
from django import forms
from .models import *

def getStudents():
  students = Student.objects.all().order_by('fname', 'lname')
  studs = []
  for stud in students:
    studs.append((str(stud), stud))
  students = tuple(studs)
  return students

STUDENTS = getStudents()

class ClassForm(forms.ModelForm):
  class Meta:
    model = Class
    fields = ('system', 'cls', 'description')

class TutorForm(forms.ModelForm):
  class Meta:
  	model = Tutor 
  	fields = ('instructor', 'insLic')

class StudentForm(forms.ModelForm):
  class Meta:
  	model = Student 
  	fields = ('idno', 'fname', 'lname', 'cls', 'address', 'telno', 'email')

class BranchForm(forms.ModelForm):
  class Meta:
    model = Branch
    fields = ('bname', )

class StudentEnrolmentForm(forms.ModelForm):
  class Meta:
    model = StudentEnrolment 
    fields = ('student', 'branch', 'date_enrol')

class ExamBookingForm(forms.ModelForm):
  class Meta:
  	model = ExamBooking  
  	fields = ('student', 'pdl', 'date', 'venue')

class PeriodForm(forms.ModelForm):
  class Meta:
  	model = Period 
  	fields = ('start', 'stop')

class RateForm(forms.ModelForm):
  class Meta:
    model = Rate 
    fields = ('clss', 'rate', 'period')

class AttendanceForm(forms.ModelForm):
  class Meta:
    model = Attendance 
    fields = ('student', 'lesson', 'typ', 'date', 'instructor')    

class PaymentForm(forms.ModelForm):
  class Meta:
  	model = Payment 
  	fields = ('student', 'amount', 'datepaid', 'mode')

class LicenseForm(forms.ModelForm):
  class Meta:
  	model = License 
  	fields = ('student','dl_type', 'dl', 'dateissued')

class DischargeForm(forms.ModelForm):
  class Meta:
  	model = Discharge 
  	fields = ('student', 'dl', 'collected', 'collector')

class PickStudentForm(forms.Form):
  students = forms.CharField(max_length=100, required=True, widget=forms.Select(choices=STUDENTS))

class PickArrearsForm(forms.Form):
  ARREARS = (
    ('all', 'All'),
    ('transport', 'Transport'),
    ('driving', 'Driving'),
    ('rent', 'Rent')
    )
  arrears = forms.CharField(max_length=100, required=True, widget=forms.Select(choices=ARREARS))
