from django.conf.urls import url, include
from transport import views

app_name = "transport"

urlpatterns = [
   url(r'^terms/$', views.term_list, name='term_list'),
   url(r'^terms/create/$', views.term_create, name='term_create'),
   url(r'^terms/(?P<pk>\d+)/update/$', views.term_update, name='term_update'),
   url(r'^terms/(?P<pk>\d+)/delete/$', views.term_delete, name='term_delete'),

   url(r'^parents/$', views.parent_list, name='parent_list'),
   url(r'^parents/create/$', views.parent_create, name='parent_create'),
   url(r'^parents/(?P<pk>[\w \']+|)/update/$', views.parent_update, name='parent_update'),
   url(r'^parents/(?P<pk>[\w \']+|)/delete/$', views.parent_delete, name='parent_delete'),

   url(r'^zones/$', views.zone_list, name='zone_list'),
   url(r'^zones/create/$', views.zone_create, name='zone_create'),
   url(r'^zones/(?P<pk>[\w ]+)/update/$', views.zone_update, name='zone_update'),
   url(r'^zones/(?P<pk>[\w ]+)/delete/$', views.zone_delete, name='zone_delete'),

   url(r'^rates/$', views.rate_list, name='rate_list'),
   url(r'^rates/create/$', views.rate_create, name='rate_create'),
   url(r'^rates/(?P<pk>\d+)/update/$', views.rate_update, name='rate_update'),
   url(r'^rates/(?P<pk>\d+)/delete/$', views.rate_delete, name='rate_delete'),

   # url(r'^classes/$', views.class_list, name='class_list'),
   # url(r'^classes/create/$', views.class_create, name='class_create'),
   # url(r'^classes/(?P<pk>\w+)/update/$', views.class_update, name='class_update'),
   # url(r'^classes/(?P<pk>\w+)/delete/$', views.class_delete, name='class_delete'),

   url(r'^estates/$', views.estate_list, name='estate_list'),
   url(r'^estates/create/$', views.estate_create, name='estate_create'),
   url(r'^estates/(?P<pk>.+?)/update/$', views.estate_update, name='estate_update'),
   url(r'^estates/(?P<pk>.+?)/delete/$', views.estate_delete, name='estate_delete'),

   url(r'^pupils/$', views.pupil_list, name='pupil_list'),
   url(r'^pupils/create/$', views.pupil_create, name='pupil_create'),
   url(r'^pupils/(?P<pk>\d+)/update/$', views.pupil_update, name='pupil_update'),
   url(r'^pupils/(?P<pk>\d+)/delete/$', views.pupil_delete, name='pupil_delete'),

   url(r'^estate_pupils/$', views.estate_pupil_list, name='estate_pupil_list'),
   url(r'^estate_pupils/create/$', views.estate_pupil_create, name='estate_pupil_create'),
   url(r'^estate_pupils/(?P<pk>\d+)/update/$', views.estate_pupil_update, name='estate_pupil_update'),
   url(r'^estate_pupils/(?P<pk>\d+)/delete/$', views.estate_pupil_delete, name='estate_pupil_delete'),
   
   url(r'^term_pupils/$', views.term_pupil_list, name='term_pupil_list'),
   url(r'^term_pupils/create/$', views.term_pupil_create, name='term_pupil_create'),
   url(r'^term_pupils/(?P<pk>\d+)/update/$', views.term_pupil_update, name='term_pupil_update'),
   url(r'^term_pupils/(?P<pk>\d+)/delete/$', views.term_pupil_delete, name='term_pupil_delete'),

   url(r'^payments/$', views.payment_list, name='payment_list'),
   url(r'^payments/create/$', views.payment_create, name='payment_create'),
   url(r'^payments/(?P<pk>\d+)/update/$', views.payment_update, name='payment_update'),
   url(r'^payments/(?P<pk>\d+)/delete/$', views.payment_delete, name='payment_delete'),

   url(r'^payment/(?P<yr>\d+)/(?P<trm>\w+)/details/$', views.paydetails, name='paydetails'),
   url(r'^payment/(?P<sumtype>\w+)/(?P<yr>\d+)/(?P<trm>\w+)/summary/$', views.paysummary,name='paysummary'),
   url(r'^payment/(?P<yr>\d+)/(?P<trm>\w+)/arrears/$', views.pupil_arrears, name='pupil_arrears'),

   url(r'^add_estate_pupils/$', views.add_est_pupils, name='add_est_pupils'),
   url(r'^add_rates/$', views.add_rates, name='add_rates'),
   url(r'^add_pupils/$', views.add_pupils, name='add_pupils'),
   url(r'^add_payments/$', views.add_payments, name='add_payments'),

   url(r'^analysis/$', views.selections, name='analysis'),
   url(r'^debts/$', views.get_debts, name='debts'),
   url(r'^getpupildetails/(?P<pupil>[\w ]+)/$', views.getpupildetails, name='getpupildetails'),
   url(r'^getsearches/$', views.getsearches, name='getsearches')
 ]
