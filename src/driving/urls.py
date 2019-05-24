from django.conf.urls import url, include
from driving import views

app_name="driving"

urlpatterns = [
   url(r'^classes/$', views.class_list, name='class_list'),
   url(r'^classes/create/$', views.class_create, name='class_create'),
   url(r'^classes/(?P<pk>\w+)/update/$', views.class_update, name='class_update'),
   url(r'^classes/(?P<pk>\w+)/delete/$', views.class_delete, name='class_delete'),

   url(r'^tutors/$', views.tutor_list, name='tutor_list'),
   url(r'^tutors/create/$', views.tutor_create, name='tutor_create'),
   url(r'^tutors/(?P<pk>\w+)/update/$', views.tutor_update, name='tutor_update'),
   url(r'^tutors/(?P<pk>\w+)/delete/$', views.tutor_delete, name='tutor_delete'),

   url(r'^students/$', views.student_list, name='student_list'),
   url(r'^students/create/$', views.student_create, name='student_create'),
   url(r'^students/(?P<pk>\w+)/update/$', views.student_update, name='student_update'),
   url(r'^students/(?P<pk>\w+)/delete/$', views.student_delete, name='student_delete'),

   url(r'^branch/$', views.branch_list, name='branch_list'),
   url(r'^branch/create/$', views.branch_create, name='branch_create'),
   url(r'^branch/(?P<pk>\w+)/update/$', views.branch_update, name='branch_update'),
   url(r'^branch/(?P<pk>\w+)/delete/$', views.branch_delete, name='branch_delete'),

   url(r'^stud_enrol/$', views.stud_enrol_list, name='stud_enrol_list'),
   url(r'^stud_enrol/create/$', views.stud_enrol_create, name='stud_enrol_create'),
   url(r'^stud_enrol/(?P<pk>\w+)/update/$', views.stud_enrol_update, name='stud_enrol_update'),
   url(r'^stud_enrol/(?P<pk>\w+)/delete/$', views.stud_enrol_delete, name='stud_enrol_delete'),

   url(r'^exam_bookings/$', views.exambooking_list, name='exambooking_list'),
   url(r'^exam_bookings/create/$', views.exambooking_create, name='exambooking_create'),
   url(r'^exam_bookings/(?P<pk>\d+)/update/$', views.exambooking_update, name='exambooking_update'),
   url(r'^exam_bookings/(?P<pk>\d+)/delete/$', views.exambooking_delete, name='exambooking_delete'),

   url(r'^periods/$', views.period_list, name='period_list'),
   url(r'^periods/create/$', views.period_create, name='period_create'),
   url(r'^periods/(?P<pk>\d+)/update/$', views.period_update, name='period_update'),
   url(r'^periods/(?P<pk>\d+)/delete/$', views.period_delete, name='period_delete'),

   url(r'^rates/$', views.rate_list, name='rate_list'),
   url(r'^rates/create/$', views.rate_create, name='rate_create'),
   url(r'^rates/(?P<pk>\d+)/update/$', views.rate_update, name='rate_update'),
   url(r'^rates/(?P<pk>\d+)/delete/$', views.rate_delete, name='rate_delete'),

   url(r'^attendances/$', views.attendance_list, name='attendance_list'),
   url(r'^attendances/create/$', views.attendance_create, name='attendance_create'),
   url(r'^attendances/(?P<pk>\d+)/update/$', views.attendance_update, name='attendance_update'),
   url(r'^attendances/(?P<pk>\d+)/delete/$', views.attendance_delete, name='attendance_delete'),

   url(r'^payments/$', views.payment_list, name='payment_list'),
   url(r'^payments/create/$', views.payment_create, name='payment_create'),
   url(r'^payments/(?P<pk>\d+)/update/$', views.payment_update, name='payment_update'),
   url(r'^payments/(?P<pk>\d+)/delete/$', views.payment_delete, name='payment_delete'),

   url(r'^licenses/$', views.license_list, name='license_list'),
   url(r'^licenses/create/$', views.license_create, name='license_create'),
   url(r'^licenses/(?P<pk>\d+)/update/$', views.license_update, name='license_update'),
   url(r'^licenses/(?P<pk>\d+)/delete/$', views.license_delete, name='license_delete'),

   url(r'^discharges/$', views.discharge_list, name='discharge_list'),
   url(r'^discharges/create/$', views.discharge_create, name='discharge_create'),
   url(r'^discharges/(?P<pk>\d+)/update/$', views.discharge_update, name='discharge_update'),
   url(r'^discharges/(?P<pk>\d+)/delete/$', views.discharge_delete, name='discharge_delete'),

   url(r'^add_payments/$', views.add_payments, name='add_payments'),
   url(r'^add_rates/$', views.add_rates, name='add_rates'),
   url(r'^add_attendance/$', views.add_attendance, name='add_attendance'),
   url(r'^add_licenses/$', views.add_licenses, name='add_licenses'),
   url(r'^add_discharges/$', views.add_discharges, name='add_discharges'),
   url(r'^add_exam_bookings/$', views.add_exam_bookings, name='add_exam_bookings'),
   url(r'^getstudentdetails/(?P<student>[\w ]+)/$', views.getstudentdetails, name='getstudentdetails'),
]
