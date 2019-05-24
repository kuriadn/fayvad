from django.shortcuts import render, get_object_or_404, render_to_response, redirect
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib import messages
import decimal
from fayvad.general import *
from .models import *
from .forms import *

# CRUD Functionality
def get_term_list(request):
    page = get_page('Terms', 'transport:term_create', 'Term')
    data = get_data_list(request,Term, TermForm, 'transport:term', page)
    return data

@login_required
def term_list(request):
    data = get_term_list(request)
    return render(request, 'list.html', {'data': data})

@login_required
def term_create(request):
    form, page = obj_create(request, TermForm, Term, 'transport:term_create')
    return save_form(request, form, Term, page, 'transport:term', 'includes/partial_create.html')

@login_required
def term_update(request, pk):
    form, page = obj_update(request, pk, TermForm, Term, 'transport:term_update')
    return save_form(request, form, Term, page, 'transport:term', 'includes/partial_update.html')

@login_required
def term_delete(request, pk):
    url = reverse('transport:term_delete', args={pk})
    data = delete_form(request, pk, TermForm, Term, url, 'transport:term',)
    return JsonResponse(data)

# Parent Object Views
def get_parent_list(request):
    page = get_page('Parents', 'transport:parent_create', 'Parent')
    data = get_data_list(request,Parent, ParentForm, 'transport:parent', page)
    return data

@login_required
def parent_list(request):
    data = get_parent_list(request)
    return render(request, 'list.html', {'data': data})

@login_required
def parent_create(request):
    form, page = obj_create(request, ParentForm, Parent, 'transport:parent_create')
    return save_form(request, form, Parent, page,'transport:parent', 'includes/partial_create.html')

@login_required
def parent_update(request, pk):
    form, page = obj_update(request, pk, ParentForm, Parent, 'transport:parent_update')
    return save_form(request, form, Parent, page,'transport:parent', 'includes/partial_update.html')

@login_required
def parent_delete(request, pk):
    url = reverse('transport:parent_delete', args={pk})
    data = delete_form(request, pk, ParentForm, Parent, url, 'transport:parent',)
    return JsonResponse(data)

# Zone Object
def get_zone_list(request):
    page = get_page('Zones', 'transport:zone_create', 'Zone')
    data = get_data_list(request,Zone, ZoneForm, 'transport:zone', page)
    return data

@login_required
def zone_list(request):
    data = get_zone_list(request)
    return render(request, 'list.html', {'data': data})

@login_required
def zone_create(request):
    form, page = obj_create(request, ZoneForm, Zone, 'transport:zone_create')
    return save_form(request, form, Zone, page, 'transport:zone', 'includes/partial_create.html')

@login_required
def zone_update(request, pk):
    form, page = obj_update(request, pk, ZoneForm, Zone, 'transport:zone_update')
    return save_form(request, form, Zone, page, 'transport:zone', 'includes/partial_update.html')

@login_required
def zone_delete(request, pk):
    url = reverse('transport:zone_delete', args={pk})
    data = delete_form(request, pk, ZoneForm, Zone, url, 'transport:zone',)
    return JsonResponse(data)

# Rate Object
def get_rate_list(request):
    page = get_page('Rates', 'transport:rate_create', 'Rate')
    data = get_data_list(request,Rate, RateForm, 'transport:rate', page)
    return data

@login_required
def rate_list(request):
    data = get_rate_list(request)
    return render(request, 'list.html', {'data': data})

@login_required
def rate_create(request):
    form, page = obj_create(request, RateForm, Rate, 'transport:rate_create')
    return save_form(request, form, Rate, page, 'transport:rate', 'includes/partial_create.html')

@login_required
def rate_update(request, pk):
    form, page = obj_update(request, pk, RateForm, Rate, 'transport:rate_update')
    return save_form(request, form, Rate, page, 'transport:rate', 'includes/partial_update.html')

@login_required
def rate_delete(request, pk):
    url = reverse('transport:rate_delete', args={pk})
    data = delete_form(request, pk, RateForm, Rate, url, 'transport:rate',)
    return JsonResponse(data)

# # Class Object
# def get_class_list(request):
#     page = get_page('Classes', 'transport:class_create', 'Class')
#     data = get_data_list(request,Class, ClassForm, 'transport:class', page)
#     return data

# @login_required
# def class_list(request):
#     data = get_class_list(request)
#     return render(request, 'list.html', {'data': data})

# @login_required
# def class_create(request):
#     form, page = obj_create(request, ClassForm, Class, 'transport:class_create')
#     return save_form(request, form, Class, page, 'transport:class', 'includes/partial_create.html')

# @login_required
# def class_update(request, pk):
#     form, page = obj_update(request, pk, ClassForm, Class, 'transport:class_update')
#     return save_form(request, form, Class, page, 'transport:class', 'includes/partial_update.html')

# @login_required
# def class_delete(request, pk):
#     url = reverse('transport:class_delete', args={pk})
#     data = delete_form(request, pk, ClassForm, Class, url, 'transport:class',)
#     return JsonResponse(data)

# Estate Object
def get_estate_list(request):
    page = get_page('Estates', 'transport:estate_create', 'Estate')
    data = get_data_list(request,Estate, EstateForm, 'transport:estate', page)
    return data

@login_required
def estate_list(request):
    data = get_estate_list(request)
    return render(request, 'list.html', {'data': data})

@login_required
def estate_create(request):
    form, page = obj_create(request, EstateForm, Estate, 'transport:estate_create')
    return save_form(request, form, Estate, page,  'transport:estate', 'includes/partial_create.html')

@login_required
def estate_update(request, pk):
    form, page = obj_update(request, pk, EstateForm, Estate, 'transport:estate_update')
    return save_form(request, form, Estate, page, 'transport:estate', 'includes/partial_update.html')

@login_required
def estate_delete(request, pk):
    url = reverse('transport:estate_delete', args={pk})
    data = delete_form(request, pk, EstateForm, Estate, url, 'transport:estate',)
    return JsonResponse(data)

# Pupil Object
def get_pupil_list(request):
    page = get_page('Pupils', 'transport:pupil_create', 'Pupil')
    data = get_data_list(request,Pupil, PupilForm, 'transport:pupil', page)
    return data

@login_required
def pupil_list(request):
    data = get_pupil_list(request)
    return render(request, 'list.html', {'data': data})

@login_required
def pupil_create(request):
    form, page = obj_create(request, PupilForm, Pupil, 'transport:pupil_create')
    return save_form(request, form, Pupil, page, 'transport:pupil', 'includes/partial_create.html')

@login_required
def pupil_update(request, pk):
    form, page = obj_update(request, pk, PupilForm, Pupil, 'transport:pupil_update')
    return save_form(request, form, Pupil, page,'transport:pupil', 'includes/partial_update.html')

@login_required
def pupil_delete(request, pk):
    url = reverse('transport:pupil_delete', args={pk})
    data = delete_form(request, pk, PupilForm, Pupil, url, 'transport:pupil',)
    return JsonResponse(data)

# EstatePupil Object
def get_estate_pupil_list(request):
    page = get_page('Estate Pupils', 'transport:estate_pupil_create', 'Estate Pupil')
    data = get_data_list(request,EstatePupil, EstatePupilForm, 'transport:estate', page)
    return data

@login_required
def estate_pupil_list(request):
    data = get_estate_pupil_list(request)
    return render(request, 'list.html', {'data': data})

@login_required
def estate_pupil_create(request):
    form, page = obj_create(request, EstatePupilForm, EstatePupil, 'transport:estate_pupil_create')
    return save_form(request, form, EstatePupil, page, 'transport:estate_pupil', 'includes/partial_create.html')

@login_required
def estate_pupil_update(request, pk):
    form, page = obj_update(request, pk, EstatePupilForm, EstatePupil, 'transport:estate_pupil_update')
    return save_form(request, form, EstatePupil, page, 'transport:estate_pupil', 'includes/partial_update.html')

@login_required
def estate_pupil_delete(request, pk):
    url = reverse('transport:estate_pupil_delete', args={pk})
    data = delete_form(request, pk, EstatePupilForm, EstatePupil, url, 'transport:estate_pupil')
    return JsonResponse(data)

#Term Pupil Object
def get_term_pupil_list(request):
    page = get_page('Term Pupils', 'transport:term_pupil_create', 'Term Pupil')
    data = get_data_list(request, TermPupil, TermPupilForm, 'transport:term_pupil', page)
    return data

@login_required
def term_pupil_list(request):
    data = get_term_pupil_list(request)
    return render(request, 'list.html', {'data': data})

@login_required
def term_pupil_create(request):
    form, page = obj_create(request, TermPupilForm, TermPupil, 'transport:term_pupil_create')
    return save_form(request, form, TermPupil, page, 'transport:term_pupil', 'includes/partial_create.html')

@login_required
def term_pupil_update(request, pk):
    form, page = obj_update(request, pk, TermPupilForm, TermPupil, 'transport:term_pupil_update')
    return save_form(request, form, TermPupil, page, 'transport:term_pupil', 'includes/partial_update.html')

@login_required
def term_pupil_delete(request, pk):
    url = reverse('transport:term_pupil_delete', args={pk})
    data = delete_form(request, pk, TermPupilForm, TermPupil, url, 'transport:term_pupil')
    return JsonResponse(data)

# Payment Object
def get_payment_list(request):
    page = get_page('Payments', 'transport:payment_create', 'Payment')
    data = get_data_list(request,Payment, PaymentForm, 'transport:payment', page)
    return data

@login_required
def payment_list(request):
    data = get_payment_list(request)
    return render(request, 'list.html', {'data': data})

@login_required
def payment_create(request):
    form, page = obj_create(request, PaymentForm, Payment, 'transport:payment_create')
    return save_form(request, form, Payment, page, 'transport:payment', 'includes/partial_create.html')

@login_required
def payment_update(request, pk):
    form, page = obj_update(request, pk, PaymentForm, Payment, 'transport:payment_update')
    return save_form(request, form, Payment, page, 'transport:payment', 'includes/partial_update.html')

@login_required
def payment_delete(request, pk):
    url = reverse('transport:payment_delete', args={pk})
    data = delete_form(request, pk, PaymentForm, Payment, url, 'transport:payment')
    return JsonResponse(data)

# Analysis Functionality
@login_required
def paysummary(request, sumtype, yr, trm):
  parents = Parent
  estates = Estate
  vans = Vehicle
  pay = Payment
  doc = []
  doc.append(sumtype)
  plist = []
  trm = get_term(yr, trm)
  if trm == "No Term Found":
    return render(request, 'nodata.html', {})
  if sumtype == 'parent':
    for parent in parents.objects.all():
      p = []
      par = parent.pname 
      p.append(par)
      p.append(getpaysumparent(pay, par, trm))
      plist.append(p)
  elif sumtype == 'estate':
    for estate in estates.objects.all():
      est = []
      es = estate.estate 
      est.append(es)
      est.append(getpaysumestate(pay, es, trm))
      plist.append(est)
  doc.append(pageddata(request, plist, 15))
  context = {'doc_list': doc}
  return render(request,'summaries.html', context)

def paydetails(request, yr, trm):
  doc=[]
  parents = Parent
  payments = Payment
  plist = []
  total = 0
  trm = get_term(yr, trm)
  if trm == "No Term Found":
    return render(request, 'nodata.html', {})
  for parent in parents.objects.all():
     par = parent.pname
     p = []
     #plist.append(par)
     p.append(par)
     p.append(parent.phone)
     ppay = getpaydetails(payments, par, 'par', trm)
     for pp in ppay:
       total += pp.amount     
     p.append(ppay)
     plist.append(p)
  parlist = pageddata(request, plist, 10)
  doc.append(parlist)
  doc.append(total)
  context = {'doc_list': doc}
  return render(request,'paydetails.html', context)

def pupil_arrears(request,yr, trm):
  if trm == 'first': trm = 'First'
  if trm == 'second': trm = 'Second'
  if trm == 'third': trm = 'Third'  
  ter = get_term(yr, trm)
  if trm == "No Term Found":
    return render(request, 'nodata.html', {})
  arrList = getAllArrears(ter)
  total = 0
  for arr in arrList:
    if type(arr[1]) == decimal.Decimal: total += arr[1]
  totLst = []
  totLst.append(pageddata(request, arrList, 15))
  totLst.append(total)
  totLst.append(ter)
  context = {'doc_list': totLst}
  return render(request, 'arrearsdetails.html', context)

@login_required
def add_est_pupils(request):
  formset = add_formset(request, EstatePupilForm, EstatePupil, 'Estate Pupils', 'transport:add_est_pupils') 
  return render(request, 'multiple.html', {'formset': formset})

@login_required
def add_rates(request):
  formset = add_formset(request, RateForm, Rate, 'Rates', 'transport:add_rates') 
  return render(request, 'multiple.html', {'formset': formset})

@login_required
def add_pupils(request):
  formset = add_formset(request, PupilForm, Pupil, 'Pupil', 'transport:add_pupils') 
  return render(request, 'multiple.html', {'formset': formset})

@login_required
def add_payments(request):
  formset = add_formset(request, PaymentForm, Payment, 'Payments', 'transport:add_payments') 
  return render(request, 'multiple.html', {'formset': formset})

@login_required
def selections(request):
  my_form = PickMonthYearForm()
  p_form = PickPeriodForm()
  t_form = PickTermForm()
  s_form = PickSummaryForm()
  forms = []
  forms.append(my_form)
  forms.append(p_form)
  forms.append(t_form)
  forms.append(s_form)
  if request.method=="POST":
    my_form = PickMonthYearForm(request.POST)
    p_form = PickPeriodForm(request.POST)
    t_form = PickTermForm(request.POST)
    s_form = PickSummaryForm(request.POST)
    if my_form.is_valid():
      data = my_form.cleaned_data
      month = data['month']
      year = data['year']
      return redirect(reverse('common:getpayments', kwargs={'year':year, 'month':month}))
    elif p_form.is_valid():
      data = p_form.cleaned_data
      start = data['start']
      end = data['end']
      if start != end:
        return redirect(reverse('common:retrievepayments', kwargs={'start':start, 'end':end}))
      else:
        return render(request, 'forms.html', {'forms': forms})
    elif s_form.is_valid():
      data = s_form.cleaned_data
      sumtype = data['sumtype']
      year = data['year']
      term = data['term']
      return redirect(reverse('transport:paysummary',kwargs={'sumtype':sumtype, 'yr':year, 'trm':term}))
    elif t_form.is_valid():
      data = t_form.cleaned_data
      yr = data['year']
      trm = data['term']
      return redirect(reverse('transport:paydetails', kwargs={'yr':yr, 'trm':trm}))
    else:
      return render(request, 'forms.html', {'forms': forms})
  else:
    return render(request, 'forms.html', {'forms': forms})

@login_required
def get_debts(request):
  from transport.forms import PickPupilForm
  from driving.forms import PickStudentForm, PickArrearsForm
  from rent.forms import PickTenantForm
  pup_form = PickPupilForm()
  stu_form = PickStudentForm()
  ten_form = PickTenantForm()
  arr_form = PickArrearsForm()
  forms = []
  forms.append(pup_form)
  forms.append(stu_form)
  forms.append(ten_form)
  forms.append(arr_form)
  if request.method=="POST":
    pup_form = PickPupilForm(request.POST)
    stu_form = PickStudentForm(request.POST)
    ten_form = PickTenantForm(request.POST)
    arr_form = PickArrearsForm(request.POST)
    if pup_form.is_valid():
      data = pup_form.cleaned_data
      pup = data['pupils']
      return redirect(reverse('transport:getpupildetails', kwargs={'pupil':pup}))
    elif arr_form.is_valid():
      data = arr_form.cleaned_data
      arr = data['arrears']
      return redirect(reverse('common:retrievearrears', kwargs={'arrtype':arr}))
    elif stu_form.is_valid():
      data = stu_form.cleaned_data
      stud = data['students']
      return redirect(reverse('driving:getstudentdetails',kwargs={'student':stud}))
    elif ten_form.is_valid():
      data = ten_form.cleaned_data
      ten = data['tenants']
      return redirect(reverse('rent:gettenantdetails', kwargs={'tenant':ten}))
    else:
      return render(request, 'debts.html', {'forms': forms})
  else:
    return render(request, 'debts.html', {'forms': forms})

@login_required
def getpupildetails(request, pupil):
  pup = pupil.split(' ')
  p = Pupil.objects.filter(fname=pup[0], sname=pup[1])[0]
  data = getPupilDetails(p)
  #print (data)
  context = {'data': data}
  return render(request,'pupildetails.html', context)

@login_required
def getsearches(request):
  pass