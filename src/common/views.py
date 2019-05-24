from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from fayvad.general import *
import calendar
from datetime import *
from .models import *
from .forms import *

# Position Object
def get_position_list(request):
    page = get_page('Positions', 'common:position_create', 'Position')
    data = get_data_list(request,Position, PositionForm, 'common:position', page)
    return data

@login_required
def position_list(request):
    data = get_position_list(request)
    return render(request, 'list.html', {'data': data})

@login_required
def position_create(request):
    form, page = obj_create(request, PositionForm, Position, 'common:position_create')
    return save_form(request, form, Position, page, 'common:position', 'includes/partial_create.html')

@login_required
def position_update(request, pk):
    form, page = obj_update(request, pk, PositionForm, Position, 'common:position_update')
    return save_form(request, form, Position, page, 'common:position', 'includes/partial_update.html')

@login_required
def position_delete(request, pk):
    url = reverse('common:position_delete', args={pk})
    data = delete_form(request, pk, PositionForm, Position, url, 'common:position',)
    return JsonResponse(data)

# Staff Object
def get_staff_list(request):
    page = get_page('Staff', 'common:staff_create', 'Staff')
    data = get_data_list(request,Staff, StaffForm, 'common:staff', page)
    return data

@login_required
def staff_list(request):
    data = get_staff_list(request)
    return render(request, 'list.html', {'data': data})

@login_required
def staff_create(request):
    form, page = obj_create(request, StaffForm, Staff, 'common:staff_create')
    return save_form(request, form, Staff, page, 'common:staff', 'includes/partial_create.html')

@login_required
def staff_update(request, pk):
    form, page = obj_update(request, pk, StaffForm, Staff, 'common:staff_update')
    return save_form(request, form, Staff, page, 'common:staff', 'includes/partial_update.html')

@login_required
def staff_delete(request, pk):
    url = reverse('common:staff_delete', args={pk})
    data = delete_form(request, pk, StaffForm, Staff, url, 'common:staff',)
    return JsonResponse(data)

# PayMode Object
def get_paymode_list(request):
    page = get_page('Payment Modes', 'common:paymode_create', 'Payment Mode')
    data = get_data_list(request,PayMode, PayModeForm, 'common:paymode', page)
    return data

@login_required
def paymode_list(request):
    data = get_paymode_list(request)
    return render(request, 'list.html', {'data': data})

@login_required
def paymode_create(request):
    form, page = obj_create(request, PayModeForm, PayMode, 'common:paymode_create')
    return save_form(request, form, PayMode, page, 'common:paymode', 'includes/partial_create.html')

@login_required
def paymode_update(request, pk):
    form, page = obj_update(request, pk, PayModeForm, PayMode, 'common:paymode_update')
    return save_form(request, form, PayMode, page, 'common:paymode', 'includes/partial_update.html')

@login_required
def paymode_delete(request, pk):
    url = reverse('common:paymode_delete', args={pk})
    data = delete_form(request, pk, PayModeForm, PayMode, url, 'common:paymode',)
    return JsonResponse(data)

# ExpenseType Object
def get_expensetype_list(request):
    page = get_page('Expense Types', 'common:expensetype_create', 'Expense Type')
    data = get_data_list(request,ExpenseType, ExpenseTypeForm, 'common:expensetype', page)
    return data

@login_required
def expensetype_list(request):
    data = get_expensetype_list(request)
    return render(request, 'list.html', {'data': data})

@login_required
def expensetype_create(request):
    form, page = obj_create(request, ExpenseTypeForm, ExpenseType, 'common:expensetype_create')
    return save_form(request, form, ExpenseType, page, 'common:expensetype', 'includes/partial_create.html')

@login_required
def expensetype_update(request, pk):
    form, page = obj_update(request, pk, ExpenseTypeForm, ExpenseType, 'common:expensetype_update')
    return save_form(request, form, ExpenseType, page, 'common:expensetype', 'includes/partial_update.html')

@login_required
def expensetype_delete(request, pk):
    url = reverse('common:expensetype_delete', args={pk})
    data = delete_form(request, pk, ExpenseTypeForm, ExpenseType, url, 'common:expensetype',)
    return JsonResponse(data)


# Driver Object
def get_driver_list(request):
    page = get_page('Drivers', 'common:driver_create', 'Driver')
    data = get_data_list(request,Driver, DriverForm, 'common:driver', page)
    return data

@login_required
def driver_list(request):
    data = get_driver_list(request)
    return render(request, 'list.html', {'data': data})

@login_required
def driver_create(request):
    form, page = obj_create(request, DriverForm, Driver, 'common:driver_create')
    return save_form(request, form, Driver, page, 'common:driver', 'includes/partial_create.html')

@login_required
def driver_update(request, pk):
    form, page = obj_update(request, pk, DriverForm, Driver, 'common:driver_update')
    return save_form(request, form, Driver, page, 'common:driver', 'includes/partial_update.html')

@login_required
def driver_delete(request, pk):
    url = reverse('common:driver_delete', args={pk})
    data = delete_form(request, pk, DriverForm, Driver, url, 'common:driver',)
    return JsonResponse(data)

# Vehicle Object
def get_vehicle_list(request):
    page = get_page('Vehicles', 'common:vehicle_create', 'Vehicle')
    data = get_data_list(request,Vehicle, VehicleForm, 'common:vehicle', page)
    return data

@login_required
def vehicle_list(request):
    data = get_vehicle_list(request)
    return render(request, 'list.html', {'data': data})

@login_required
def vehicle_create(request):
    form, page = obj_create(request, VehicleForm, Vehicle, 'common:vehicle_create')
    return save_form(request, form, Vehicle, page, 'common:vehicle', 'includes/partial_create.html')

@login_required
def vehicle_update(request, pk):
    form, page = obj_update(request, pk, VehicleForm, Vehicle, 'common:vehicle_update')
    return save_form(request, form, Vehicle, page, 'common:vehicle', 'includes/partial_update.html')

@login_required
def vehicle_delete(request, pk):
    url = reverse('common:vehicle_delete', args={pk})
    data = delete_form(request, pk, VehicleForm, Vehicle, url, 'common:vehicle',)
    return JsonResponse(data)

# Expense Object
def get_expense_list(request):
    page = get_page('Expenses', 'common:expense_create', 'Expense')
    data = get_data_list(request,Expense, ExpenseForm, 'common:expense', page)
    return data

@login_required
def expense_list(request):
    data = get_expense_list(request)
    return render(request, 'list.html', {'data': data})

@login_required
def expense_create(request):
    form, page = obj_create(request, ExpenseForm, Expense, 'common:expense_create')
    return save_form(request, form, Expense, page, 'common:expense', 'includes/partial_create.html')

@login_required
def expense_update(request, pk):
    form, page = obj_update(request, pk, ExpenseForm, Expense, 'common:expense_update')
    return save_form(request, form, Expense, page, 'common:expense', 'includes/partial_update.html')

@login_required
def expense_delete(request, pk):
    url = reverse('common:expense_delete', args={pk})
    data = delete_form(request, pk, ExpenseForm, Expense, url, 'common:expense',)
    return JsonResponse(data)

# Trip Object
def get_trip_list(request):
    page = get_page('Trips', 'common:trip_create', 'Trip')
    data = get_data_list(request,Trip, TripForm, 'common:trip', page)
    return data

@login_required
def trip_list(request):
    data = get_trip_list(request)
    return render(request, 'list.html', {'data': data})

@login_required
def trip_create(request):
    form, page = obj_create(request, TripForm, Trip, 'common:trip_create')
    return save_form(request, form, Trip, page, 'common:trip', 'includes/partial_create.html')

@login_required
def trip_update(request, pk):
    form, page = obj_update(request, pk, TripForm, Trip, 'common:trip_update')
    return save_form(request, form, Trip, page, 'common:trip', 'includes/partial_update.html')

@login_required
def trip_delete(request, pk):
    url = reverse('common:trip_delete', args={pk})
    data = delete_form(request, pk, TripForm, Trip, url, 'common:trip',)
    return JsonResponse(data)

def getMonthIndex(month):
  months = []
  for i in range (13):
    months.append(calendar.month_name[i])
  return months.index(month.title())

@login_required
def getpayments(request, year, month):
  mon = getMonthIndex(month)
  yr = int(year)
  days = calendar.mdays[mon]
  if mon == 2:
    if calendar.isleap(yr):
      days = 29
    else:
      days = 28
  start = date(yr, mon, 1)
  end = date(yr, mon, days)
  data = getPayment(start, end)
  return render(request, 'all_payments.html', {'data': data})

@login_required
def retrievepayments(request, start, end):
  data = getPayment(start, end)
  return render(request, 'all_payments.html', {'data': data})

@login_required
def retrievearrears(request, arrtype):
  data = getArrears(arrtype)
  return render(request, 'all_arrears.html', {'data': data})

@login_required
def add_expenses(request):
  formset = add_formset(request, ExpenseForm, Expense, 'Expenses', 'common:add_expenses') 
  return render(request, 'multiple.html', {'formset': formset})

@login_required
def add_trips(request):
  formset = add_formset(request, TripForm, Trip, 'Trips', 'common:add_trips') 
  return render(request, 'multiple.html', {'formset': formset})

@login_required
def getexpenses(request, start, end):
  data = getexpensedata(start, end)
  return render(request, 'expenses.html', {'data': data})

@login_required
def getexpense(request, expense, start, end):
  data = getexpensedata(start, end, expense)
  return render(request, 'expenses.html', {'data': data})

@login_required
def get_expenses(request):
  my_form = PickPeriodForm()
  p_form = PickExpPeriodForm()
  t_form = PickPeriodForm()
  forms = []
  forms.append(my_form)
  forms.append(p_form)
  forms.append(t_form)
  if request.method=="POST":
    my_form = PickPeriodForm(request.POST)
    p_form = PickExpPeriodForm(request.POST)
    t_form = PickPeriodForm(request.POST)
    print('my_form: {0}; p_form: {1}; t_form: {2}'.format(my_form.is_valid(), p_form.is_valid(), t_form.is_valid()))
    if my_form.is_valid():
      data = my_form.cleaned_data
      start = data['start']
      end = data['end']
      if start != end:
        return redirect(reverse('common:getexpenses', kwargs={'start':start, 'end':end}))
      else:
        return render(request, 'forms_exp.html', {'forms': forms})
    elif p_form.is_valid():
      data = p_form.cleaned_data
      start = data['start_date']
      end = data['end_date']
      exp = data['expense']
      print('start: {0}; end: {1}; expense: {2}'.format(start, end, exp))
      if start != end:
        return redirect(reverse('common:getexpense', kwargs={'start':start, 'end':end, 'expense': exp}))
      else:
        return render(request, 'forms_exp.html', {'forms': forms})
    elif s_form.is_valid():
      data = s_form.cleaned_data
      start = data['start']
      end = data['end']
      if start != end:
        return redirect(reverse('common:getexpenses', kwargs={'start':start, 'end':end}))
      else:
        return render(request, 'forms_exp.html', {'forms': forms})
    elif t_form.is_valid():
      data = t_form.cleaned_data
      start = data['start']
      end = data['end']
      if start != end:
        return redirect(reverse('common:getexpenses', kwargs={'start':start, 'end':end}))
      else:
        return render(request, 'forms_exp.html', {'forms': forms})
    else:
      return render(request, 'forms_exp.html', {'forms': forms})
  else:
    return render(request, 'forms_exp.html', {'forms': forms})