from django.conf.urls import url, include
from rent import views

app_name = "rent"

urlpatterns = [
   url(r'^tenants/$', views.tenant_list, name='tenant_list'),
   url(r'^tenants/create/$', views.tenant_create, name='tenant_create'),
   url(r'^tenants/(?P<pk>\d+)/update/$', views.tenant_update, name='tenant_update'),
   url(r'^tenants/(?P<pk>\d+)/delete/$', views.tenant_delete, name='tenant_delete'),

   url(r'^rooms/$', views.room_list, name='room_list'),
   url(r'^rooms/create/$', views.room_create, name='room_create'),
   url(r'^rooms/(?P<pk>\d+)/update/$', views.room_update, name='room_update'),
   url(r'^rooms/(?P<pk>\d+)/delete/$', views.room_delete, name='room_delete'),

   url(r'^rent_regimes/$', views.rent_regime_list, name='rent_regime_list'),
   url(r'^rent_regimes/create/$', views.rent_regime_create, name='rent_regime_create'),
   url(r'^rent_regimes/(?P<pk>\d+)/update/$', views.rent_regime_update, name='rent_regime_update'),
   url(r'^rent_regimes/(?P<pk>\d+)/delete/$', views.rent_regime_delete, name='rent_regime_delete'),

   url(r'^room_tenants/$', views.roomtenant_list, name='roomtenant_list'),
   url(r'^room_tenants/create/$', views.roomtenant_create, name='roomtenant_create'),
   url(r'^room_tenants/(?P<pk>\d+)/update/$', views.roomtenant_update, name='roomtenant_update'),
   url(r'^room_tenants/(?P<pk>\d+)/delete/$', views.roomtenant_delete, name='roomtenant_delete'),
   url(r'^add_room_tenants/$', views.add_room_tenants, name='add_room_tenants'),

   url(r'^payments/$', views.payment_list, name='payment_list'),
   url(r'^payments/create/$', views.payment_create, name='payment_create'),
   url(r'^payments/(?P<pk>\d+)/update/$', views.payment_update, name='payment_update'),
   url(r'^payments/(?P<pk>\d+)/delete/$', views.payment_delete, name='payment_delete'),

   url(r'^getstenantdetails/(?P<tenant>[\w ]+)/$', views.gettenantdetails, name='gettenantdetails'),
]
