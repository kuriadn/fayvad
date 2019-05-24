from django.contrib import admin
from .models import * 

class VehicleAdmin(admin.ModelAdmin):
  fields = ('regno', 'dueinsurance',)
  list_display = ('regno', 'dueinsurance',)
  list_filter = ('regno', 'dueinsurance',)
  list_per_page = 10

class DriverAdmin(admin.ModelAdmin):
  fields = ('idno', 'fname', 'lname', 'address', 'telno', 'email', 'duelicense', )  
  list_display = ('idno', 'fname', 'lname', 'address', 'telno', 'email', 'duelicense', )  
  list_filter = ('idno', 'fname', 'lname', 'address', 'telno', 'email', 'duelicense',)  
  list_per_page = 10

class ExpenseAdmin(admin.ModelAdmin):
  fields = ('exptype', 'amount', 'date', 'vehicle',)
  list_display = ('exptype', 'amount', 'date', 'vehicle',)
  list_filter = ('exptype', 'amount', 'date', 'vehicle',)
  list_per_page = 10

class TripAdmin(admin.ModelAdmin):
  fields = ('van', 'amount', 'datepaid', 'desc',)
  list_display = ('van', 'amount', 'datepaid', 'desc',)
  list_filter = ('van', 'amount', 'datepaid','desc',)
  list_per_page = 10

#admin.site.unregister(PayMode)
#admin.site.register(PayMode)
admin.site.register(Vehicle, VehicleAdmin)
admin.site.register(Driver, DriverAdmin)
admin.site.register(Expense, ExpenseAdmin)
admin.site.register(Trip, TripAdmin)
#admin.site.register(ExpenseType)
admin.site.register(Position)