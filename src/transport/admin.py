from django.contrib import admin
from .models import *

class RateAdmin(admin.ModelAdmin):
   fields = ('zone', 'rate', 'term',)
   list_display = ('zone', 'rate', 'term',)
   list_filter = ('zone', 'rate', 'term',)
   list_per_page = 20
  
class ZoneAdmin(admin.ModelAdmin):
   fields = ('zone',)
   list_display = ('zone',)
   list_filter = ('zone',)
   list_per_page = 20

class ParentAdmin(admin.ModelAdmin):
  fields = ('pname', 'phone',)
  list_display = ('pname', 'phone',)
  list_filter = ('pname', 'phone',)
  list_per_page = 20

class EstateAdmin(admin.ModelAdmin):
  fields = ('estate', 'zone',)
  list_display = ('estate', 'zone',)
  list_filter = ('estate', 'zone',)
  list_per_page = 20

class PupilAdmin(admin.ModelAdmin):
  fields = ('fname', 'sname','parent',)
  list_display = ('fname', 'sname','parent',)
  list_filter = ('fname', 'sname','parent',)
  list_per_page = 20

class PaymentAdmin(admin.ModelAdmin):
  fields = ('pupil', 'datepaid', 'amount', 'mode',)
  list_display = ('pupil', 'datepaid', 'amount', 'mode',)
  list_filter = ('pupil', 'datepaid', 'amount', 'mode',)
  list_per_page = 20

class EstatePupilAdmin(admin.ModelAdmin):
  fields = ('pupil', 'estate',)
  list_display = ('pupil', 'estate',)
  list_filter = ('pupil', 'estate',)
  list_per_page = 20

class TermPupilAdmin(admin.ModelAdmin):
  fields = ('pupil', 'term',)
  list_display = ('pupil', 'term',)
  list_filter = ('pupil', 'term',)
  list_per_page = 20

admin.site.register(Zone, ZoneAdmin)
admin.site.register(Rate, RateAdmin)
# admin.site.register(Class)
admin.site.register(Term)
admin.site.register(EstatePupil, EstatePupilAdmin)
admin.site.register(TermPupil, TermPupilAdmin)
admin.site.register(Parent, ParentAdmin)
admin.site.register(Estate, EstateAdmin)
admin.site.register(Pupil, PupilAdmin)
admin.site.register(Payment, PaymentAdmin)
