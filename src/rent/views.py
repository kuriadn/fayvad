from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from fayvad.general import *
from .models import *
from .forms import *

# Tenant Object
def get_tenant_list(request):
    page = get_page('Tenants', 'rent:tenant_create', 'Tenant')
    data = get_data_list(request,Tenant, TenantForm, 'rent:tenant', page)
    return data

@login_required
def tenant_list(request):
    data = get_tenant_list(request)
    return render(request, 'list.html', {'data': data})

@login_required
def tenant_create(request):
    form, page = obj_create(request, TenantForm, Tenant, 'rent:tenant_create')
    return save_form(request, form, Tenant, page, 'rent:tenant', 'includes/partial_create.html')

@login_required
def tenant_update(request, pk):
    form, page = obj_update(request, pk, TenantForm, Tenant, 'rent:tenant_update')
    return save_form(request, form, Tenant, page, 'rent:tenant', 'includes/partial_update.html')

@login_required
def tenant_delete(request, pk):
    url = reverse('rent:tenant_delete', args={pk})
    data = delete_form(request, pk, TenantForm, Tenant, url, 'rent:tenant',)
    return JsonResponse(data)

# Room Object
def get_room_list(request):
    page = get_page('Rooms', 'rent:room_create', 'Room')
    data = get_data_list(request,Room, RoomForm, 'rent:room', page)
    return data

@login_required
def room_list(request):
    data = get_room_list(request)
    return render(request, 'list.html', {'data': data})

@login_required
def room_create(request):
    form, page = obj_create(request, RoomForm, Room, 'rent:room_create')
    return save_form(request, form, Room, page, 'rent:room', 'includes/partial_create.html')

@login_required
def room_update(request, pk):
    form, page = obj_update(request, pk, RoomForm, Room, 'rent:room_update')
    return save_form(request, form, Room, page, 'rent:room', 'includes/partial_update.html')

@login_required
def room_delete(request, pk):
    url = reverse('rent:room_delete', args={pk})
    data = delete_form(request, pk, RoomForm, Room, url, 'rent:room',)
    return JsonResponse(data)

# Rent_Regime Object
def get_rent_regime_list(request):
    page = get_page('Rent Regimes', 'rent:rent_regime_create', 'Rent Regime')
    data = get_data_list(request,Rent_Regime, RentRegimeForm, 'rent:rent_regime', page)
    return data

@login_required
def rent_regime_list(request):
    data = get_rent_regime_list(request)
    return render(request, 'list.html', {'data': data})

@login_required
def rent_regime_create(request):
    form, page = obj_create(request, RentRegimeForm, Rent_Regime, 'rent:rent_regime_create')
    return save_form(request, form, Rent_Regime, page, 'rent:rent_regime', 'includes/partial_create.html')

@login_required
def rent_regime_update(request, pk):
    form, page = obj_update(request, pk, RentRegimeForm, Rent_Regime, 'rent:rent_regime_update')
    return save_form(request, form, Rent_Regime, page, 'rent:rent_regime', 'includes/partial_update.html')

@login_required
def rent_regime_delete(request, pk):
    url = reverse('rent:rent_regime_delete', args={pk})
    data = delete_form(request, pk, RentRegimeForm, Rent_Regime, url, 'rent:rent_regime',)
    return JsonResponse(data)

# RoomTenant Object
def get_roomtenant_list(request):
    page = get_page('Room Tenants', 'rent:roomtenant_create', 'Room Tenant')
    data = get_data_list(request,Room_Tenant, Room_TenantForm, 'rent:roomtenant', page)
    return data

@login_required
def roomtenant_list(request):
    data = get_roomtenant_list(request)
    return render(request, 'list.html', {'data': data})

@login_required
def roomtenant_create(request):
    form, page = obj_create(request, Room_TenantForm, Room_Tenant, 'rent:roomtenant_create')
    return save_form(request, form, Room_Tenant, page, 'rent:roomtenant', 'includes/partial_create.html')

@login_required
def roomtenant_update(request, pk):
    form, page = obj_update(request, pk, Room_TenantForm, Room_Tenant, 'rent:roomtenant_update')
    return save_form(request, form, Room_Tenant, page, 'rent:roomtenant', 'includes/partial_update.html')

@login_required
def roomtenant_delete(request, pk):
    url = reverse('rent:roomtenant_delete', args={pk})
    data = delete_form(request, pk, Room_TenantForm, Room_Tenant, url, 'rent:roomtenant',)
    return JsonResponse(data)

# Payment Object
def get_payment_list(request):
    page = get_page('Payments', 'rent:payment_create', 'Payment')
    data = get_data_list(request,Payment, PaymentForm, 'rent:payment', page)
    return data

@login_required
def payment_list(request):
    data = get_payment_list(request)
    return render(request, 'list.html', {'data': data})

@login_required
def payment_create(request):
    form, page = obj_create(request, PaymentForm, Payment, 'rent:payment_create')
    return save_form(request, form, Payment, page, 'rent:payment', 'includes/partial_create.html')

@login_required
def payment_update(request, pk):
    form, page = obj_update(request, pk, PaymentForm, Payment, 'rent:payment_update')
    return save_form(request, form, Payment, page, 'rent:payment', 'includes/partial_update.html')

@login_required
def payment_delete(request, pk):
    url = reverse('rent:payment_delete', args={pk})
    data = delete_form(request, pk, PaymentForm, Payment, url, 'rent:payment',)
    return JsonResponse(data)

@login_required
def add_room_tenants(request):
  formset = add_formset(request, Room_TenantForm, Room_Tenant, 'Room Tenants', 'rent:add_room_tenants') 
  return render(request, 'multiple.html', {'formset': formset})

@login_required
def gettenantdetails(request, tenant):
  ten = Tenant.objects.filter(name=tenant)[0]
  data = getTenantDetails(ten)
  print (data)
  context = {'data': data}
  return render(request,'tenantdetails.html', context)
