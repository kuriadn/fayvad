from django.conf.urls import url, include
from common import views

app_name="common"

urlpatterns = [
   url(r'^positions/$', views.position_list, name='position_list'),
   url(r'^positions/create/$', views.position_create, name='position_create'),
   url(r'^positions/(?P<pk>[\w ]+)/update/$', views.position_update, name='position_update'),
   url(r'^positions/(?P<pk>[\w ]+)/delete/$', views.position_delete, name='position_delete'),

   url(r'^staff/$', views.staff_list, name='staff_list'),
   url(r'^staff/create/$', views.staff_create, name='staff_create'),
   url(r'^staff/(?P<pk>\w+)/update/$', views.staff_update, name='staff_update'),
   url(r'^staff/(?P<pk>\w+)/delete/$', views.staff_delete, name='staff_delete'),

   url(r'^paymodes/$', views.paymode_list, name='paymode_list'),
   url(r'^paymodes/create/$', views.paymode_create, name='paymode_create'),
   url(r'^paymodes/(?P<pk>\w+)/update/$', views.paymode_update, name='paymode_update'),
   url(r'^paymodes/(?P<pk>\w+)/delete/$', views.paymode_delete, name='paymode_delete'),

   url(r'^expensetypes/$', views.expensetype_list, name='expensetype_list'),
   url(r'^expensetypes/create/$', views.expensetype_create, name='expensetype_create'),
   url(r'^expensetypes/(?P<pk>\d+)/update/$', views.expensetype_update, name='expensetype_update'),
   url(r'^expensetypes/(?P<pk>\d+)/delete/$', views.expensetype_delete, name='expensetype_delete'),

   url(r'^drivers/$', views.driver_list, name='driver_list'),
   url(r'^drivers/create/$', views.driver_create, name='driver_create'),
   url(r'^drivers/(?P<pk>\w+)/update/$', views.driver_update, name='driver_update'),
   url(r'^drivers/(?P<pk>\w+)/delete/$', views.driver_delete, name='driver_delete'),

   url(r'^vehicles/$', views.vehicle_list, name='vehicle_list'),
   url(r'^vehicles/create/$', views.vehicle_create, name='vehicle_create'),
   url(r'^vehicles/(?P<pk>\w+)/update/$', views.vehicle_update, name='vehicle_update'),
   url(r'^vehicles/(?P<pk>\w+)/delete/$', views.vehicle_delete, name='vehicle_delete'),

   url(r'^expenses/$', views.expense_list, name='expense_list'),
   url(r'^expenses/create/$', views.expense_create, name='expense_create'),
   url(r'^expenses/(?P<pk>\d+)/update/$', views.expense_update, name='expense_update'),
   url(r'^expenses/(?P<pk>\d+)/delete/$', views.expense_delete, name='expense_delete'),

   url(r'^trips/$', views.trip_list, name='trip_list'),
   url(r'^trips/create/$', views.trip_create, name='trip_create'),
   url(r'^trips/(?P<pk>\w+)/update/$', views.trip_update, name='trip_update'),
   url(r'^trips/(?P<pk>\w+)/delete/$', views.trip_delete, name='trip_delete'),

   url(r'^payments/(?P<year>\d+)/(?P<month>\w+)/$', views.getpayments, name='getpayments'),
   url(r'^retrievepayments/(?P<start>\d{4}-\d{2}-\d{2})/(?P<end>\d{4}-\d{2}-\d{2})/$', views.retrievepayments, name='retrievepayments'),
   url(r'^retrievearrears/(?P<arrtype>\w+)/$', views.retrievearrears, name='retrievearrears'),
   url(r'^add_expenses/$', views.add_expenses, name='add_expenses'),
   url(r'^add_trips/$', views.add_trips, name='add_trips'),

   url(r'^getexpense/(?P<expense>[\w ]+)/(?P<start>\d{4}-\d{2}-\d{2})/(?P<end>\d{4}-\d{2}-\d{2})/$', views.getexpense, name='getexpense'),
   url(r'^getexpenses/(?P<start>\d{4}-\d{2}-\d{2})/(?P<end>\d{4}-\d{2}-\d{2})/$', views.getexpenses, name='getexpenses'),
   url(r'^get_expenses/$', views.get_expenses, name='get_expenses'),
   
]
