from django.contrib import admin
from .models import *

class TutorAdmin(admin.ModelAdmin):
  fields = ('instructor', 'insLic',)
  list_display = ('instructor', 'insLic',)
  list_filter = ('instructor', 'insLic',)
  search_fields = ('instructor', 'insLic',)
  list_per_page = 10

class StudentAdmin(admin.ModelAdmin):
  fields = ('idno', 'fname', 'lname', 'address', 'telno', 'email', 'cls',)
  list_display = ('idno', 'fname', 'lname', 'address', 'telno', 'cls',)
  list_filter = ('idno', 'fname', 'lname', 'address', 'telno', 'cls',)
  search_fields = ('idno', 'fname', 'lname', 'address', 'telno', 'cls',)
  list_per_page = 10

class ExamBookingAdmin(admin.ModelAdmin):
  fields = ('student', 'pdl', 'date', 'venue',)
  list_display = ('student', 'pdl', 'date', 'venue',)
  list_filter = ('student', 'pdl', 'date', 'venue',)
  list_per_page = 10

class RateAdmin(admin.ModelAdmin):
  fields = ('clss', 'rate', 'period',)
  list_display = ('clss', 'rate', 'period',)
  list_filter = ('clss', 'rate', 'period',)
  list_per_page = 10

class PaymentAdmin(admin.ModelAdmin):
  fields = ('student', 'datepaid', 'amount', 'mode',)
  list_display = ('student', 'datepaid', 'amount', 'mode',)
  list_filter = ('student', 'datepaid', 'amount', 'mode',)
  list_per_page = 10

class AttendanceAdmin(admin.ModelAdmin):
  fields = ('student', 'lesson', 'typ', 'date', 'instructor',)
  list_display = ('student', 'lesson', 'typ', 'date', 'instructor',)
  list_filter = ('student', 'lesson', 'typ', 'date', 'instructor',)
  list_per_page = 10

class DischargeAdmin(admin.ModelAdmin):
  fields = ('student', 'dl', 'collected', 'collector',)
  list_display = ('student', 'dl', 'collected', 'collector',)
  list_filter = ('student', 'dl', 'collected', 'collector',)
  list_per_page = 10

admin.site.register(Class)
admin.site.register(Tutor, TutorAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(ExamBooking, ExamBookingAdmin)
admin.site.register(Period)
admin.site.register(Rate, RateAdmin)
admin.site.register(Payment, PaymentAdmin)
admin.site.register(PayMode)
admin.site.register(ExpenseType)
admin.site.register(Attendance, AttendanceAdmin)
admin.site.register(Discharge, DischargeAdmin)
