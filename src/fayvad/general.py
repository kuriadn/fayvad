from django.shortcuts import render, get_object_or_404
from django.db.models import * 
import decimal
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.urls import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger 
from datetime import *
from django.forms import formset_factory
from django.db import IntegrityError, transaction
from transport.models import Pupil, EstatePupil, TermPupil, Term, Rate, Zone, Payment as TransportPay
from driving.models import Class, Student, StudentEnrolment, Attendance, Payment as DrivingPay, Rate as DrRate
from rent.models import Tenant, Room_Tenant, Rent_Regime, Payment as RentPay
from common.models import Trip, Expense, ExpenseType

def preppaydata(Model, desc, start, end):
  objs = Model.objects.filter(datepaid__gte=start, datepaid__lte=end)
  paid = objs.values('amount').annotate(paid=Sum('amount')).order_by('paid')
  total = 0
  for i in range(len(paid)):
    total += paid[i]['paid']
  data = []
  data.append(desc)
  data.append(objs)
  data.append(total)
  return data

def getexpensedata(start, end, exp='all'):
  if exp == 'all':
    expType = ExpenseType.objects.all()
  else:
    expType = ExpenseType.objects.filter(exp=exp)
  data = []
  print ('Expense: {0}'.format(exp))
  totals = 0
  duration = []
  duration.append(start)
  duration.append(end)
  data.append(duration)
  expdata = []
  for xpTy in expType:
    dt = []
    exp = Expense.objects.filter(exptype=xpTy, date__lte=end, date__gte=start)
    paid = exp.values('amount').annotate(paid=Sum('amount')).order_by('paid')
    total = 0
    for i in range(len(paid)):
      total += paid[i]['paid']
    dt.append(xpTy)
    dt.append(exp)
    dt.append(total)
    totals += total
    expdata.append(dt)
  data.append(expdata)
  data.append(totals)
  return data

def getPayment(start, end):
  tran = preppaydata(TransportPay, 'Pupil Payments', start, end)
  rent = preppaydata(RentPay, 'Tenant Payments', start, end)
  driv = preppaydata(DrivingPay, 'Student Payments', start, end)
  trip = preppaydata(Trip, 'Trip Payments', start, end)
  data = []
  data.append(tran)
  data.append(rent)
  data.append(driv)
  data.append(trip)
  data.append('{0} - {1}'.format(start,end))
  return data

def prepEstate(trm):
  pups = Pupil.objects.all()
  estTerm = EstatePupil.objects.filter(term=trm)
  puplist = []
  misspup = []
  for est in estTerm:
    puplist.append(est.pupil)
  for pup in pups:
    if pup not in puplist:
       misspup.append(pup)
  return misspup

class terms():

  def __init__(self):
    self.term = ''
    self.start = ''
    self.end = ''

  def getTerm(self, yr, tm):
    self.term = tm
    yea = int(yr)
    if tm == 'First':
      self.start = date(yea, 1, 1)
      self.end = date(yea, 4, 15)
    elif tm == 'Second':
      self.start = date(yea, 5, 1)
      self.end = date(yea, 8, 15)
    elif tm == 'Third':
      self.start = date(yea, 9, 1)
      self.end = date(yea, 12, 15)
    return self

def get_term(yr, trm):
  if trm == 'first': trm = 'First'
  if trm == 'second': trm = 'Second'
  if trm == 'third': trm = 'Third'  
  ter = terms().getTerm(yr, trm)
  tm = Term.objects.filter(term=trm, year=yr)
  if len(tm) > 0:
    return tm[0]
  else:
    return "No Term Found"

def getTransportDue(pup):
  estPup = EstatePupil.objects.filter(pupil=pup)
  termPup = TermPupil.objects.filter(pupil=pup)
  due = 0
  for trm in termPup:
    try:
      rate = Rate.objects.filter(zone=estPup[0].estate.zone, term=trm.term)
      if len(rate) > 0: due += rate[0].rate
    except BaseException: 
      print (trm, ' --> Issue encountered')
      due = due
  return due

def getTransportPay(pup):
  objs = TransportPay.objects.filter(pupil=pup)
  return getPaymentsDone(objs)

def getTransportArrears(pup):
  due = getTransportDue(pup)
  pay = getTransportPay(pup)
  return due - pay

def getPupilArrears(pup, trm):
    term = terms().getTerm(trm.year, trm.term)
    pupPay = [x for x in TransportPay.objects.filter(pupil=pup, datepaid__gte=term.start, datepaid__lte=term.end)]
    estPup = EstatePupil.objects.filter(pupil=pup, estate__zone__rate__term=trm)
    rate = 'Not a Customer or not yet defined!'
    if estPup.count() > 0:
      rate = Rate.objects.filter(zone=estPup[0].estate.zone, term=trm)[0].rate
      amount = 0
      if len(pupPay) > 0:
        for pay in pupPay:
          amount += pay.amount
      return rate - amount
    else:
      return rate

def getTripPayments(start, end):
  pay = Trip.objects.filter(date_gte=start, date__lte=end)
  return pay

def getAllPupilArrears(term):
    pups = Pupil.objects.all().order_by('sname')
    pupList = []
    for pup in pups:
      pp = []
      pp.append(pup.fname + ' ' + pup.sname)
      arr = getPupilArrears(pup, term)
      add = False
      if type(arr) == decimal.Decimal:
        if arr > 0: 
          pp.append(arr)
          add = True
      else:
        pp.append(arr)
        add = True
      if add: pupList.append(pp)
    return pupList

def getpaydetails(pay, obj, typ, term='all'):
  if term == 'all':
    if typ == 'par':
      return pay.objects.filter(pupil__parent__pname=obj)
    else:
      return pay.objects.filter(pupil__estatepupil__estate__estate=obj)
  else: 
    ter = terms().getTerm(term.year, term.term)
    if typ == 'par':
      return pay.objects.filter(pupil__parent__pname=obj, datepaid__gte=ter.start, datepaid__lte=ter.end)
    else:
      return pay.objects.filter(pupil__estatepupil__estate__estate=obj, datepaid__gte=ter.start, datepaid__lte=ter.end)

def getpaysumparent(pay,par, term='all'):
   pp = getpaydetails(pay, par, 'par', term)
   pp = pp.values('amount').annotate(paid=Sum('amount')).order_by('paid')
   if len(pp) > 0: 
     sm = 0
     for i in range(len(pp)):
       sm += pp[i]['paid']
     return sm
   else: return 0

def getpaysumestate(pay,est, term='all'):
   pp = getpaydetails(pay, est, 'est', term)
   pp = pp.values('amount').annotate(paid=Sum('amount')).order_by('paid')
   if len(pp) > 0: 
     sm = 0
     for i in range(len(pp)):
       sm += pp[i]['paid']
     return sm
   else: return 0

def getPaymentsDone(objs):
  paid = objs.values('amount').annotate(paid=Sum('amount')).order_by('paid')
  total = 0
  for i in range(len(paid)):
    total += paid[i]['paid']
  return total

def getRentPayment(tenant):
  objs = RentPay.objects.filter(tenant=tenant)
  return getPaymentsDone(objs)

def getRentDue(tenant):
  rmtenant = Room_Tenant.objects.filter(tenant=tenant)
  if len(rmtenant) <=0: return 0
  commence = rmtenant[0].commencement
  today = datetime.now()
  duration = int((datetime.date(datetime.now()) - commence).days/30)
  st_rate = Rent_Regime.objects.filter(beg_date__lte=commence, end_date__gte=commence).order_by('beg_date')[0]
  mon_rem = int((st_rate.end_date-commence).days/30)
  rates = list(Rent_Regime.objects.filter(end_date__lte=today))
  rates.append(list(Rent_Regime.objects.filter(beg_date__lte=today, end_date__gte=today))[0])
  due = 0
  due = mon_rem * st_rate.amount
  rem_mon = duration - mon_rem
  
  if len(rates) > 0:
    for item in rates:
      if item.beg_date < st_rate.beg_date:
        rates.remove(item)

    # remove st_rate
    rates.remove(rates[0])
    for i in range(len(rates)-1):  
      months = int((rates[i].end_date - rates[i].beg_date).days/30)
      due += months * rates[i].amount
      rem_mon -= months

  # compute for current year
    due += rem_mon * rates[len(rates)-1].amount
  return due 

# Rent Arrears
def getRentArrears(tenant):
  due = getRentDue(tenant)
  pay = getRentPayment(tenant)
  return due - pay

def getDrivingDue(student):
  due = 0
  cls = Student.objects.filter(fname=student.fname, lname=student.lname).values('cls')
  if len(cls) > 0:
    clss = cls[0]
  else: return due 
  cls = Class.objects.filter(cls=clss['cls'])
  if len(cls) > 0:
    rate = DrRate.objects.filter(clss=cls[0])
    if len(rate) > 0:
      due = rate[0].rate
  return due

def getDrivingPayment(student):
  objs = DrivingPay.objects.filter(student=student)
  return getPaymentsDone(objs)

# Driving School Arrears
def getDrivingArrears(student):
  due = getDrivingDue(student)
  pay = getDrivingPayment(student)
  return due - pay

# prepare arrears data
def preparrdata(RefModel, PayModel, Type, desc):
  total = 0
  objArr = []
  objs = RefModel.objects.all()
  if Type == 'Transport':
    for obj in objs:
      obAr = []
      arr = getTransportArrears(obj)
      obAr.append(obj.fname + ' ' + obj.sname)
      estpup = EstatePupil.objects.filter(pupil=obj)
      if len(estpup) > 0:
        ora = estpup[0].estate
      else:
        ora = 'Estate not defined'
      obAr.append(ora)
      obAr.append(arr)
      objArr.append(obAr)
      total += arr
  elif Type == 'Driving':
    for obj in objs:
      obAr = []
      arr = getDrivingArrears(obj)
      obAr.append(obj.fname + ' ' + obj.lname)
      studenrol = StudentEnrolment.objects.filter(student=obj)
      if len(studenrol) > 0:
        ora = studenrol[0].branch
      else:
        ora = 'Branch not defined'
      obAr.append(ora)
      obAr.append(arr)
      objArr.append(obAr)
      total += arr
  elif Type == 'Rent':
    for obj in objs:
      obAr = []
      arr = getRentArrears(obj)
      obAr.append(obj.name)
      rmten = Room_Tenant.objects.filter(tenant=obj)
      if len(rmten) > 0:
        ora = rmten[0].room.site + ' ' + rmten[0].room.room
      else:
        ora = 'Room Tenant not defined'
      obAr.append(ora)
      obAr.append(arr)
      objArr.append(obAr)
      total += arr
  data = []
  data.append(desc)
  data.append(objArr)
  data.append(total)
  return data

def makeEmptyArrears(desc):
  data = []
  data.append(desc)
  data.append([])
  data.append(0)
  return data

def getArrears(arrtype):
  data = []
  if arrtype=='all':
    tran = preparrdata(Pupil, TransportPay, 'Transport', 'Pupil Arrears')
    rent = preparrdata(Tenant, RentPay, 'Rent', 'Tenant Arrears')
    driv = preparrdata(Student, DrivingPay, 'Driving', 'Student Arrears')
  if arrtype == 'transport':
    tran = preparrdata(Pupil, TransportPay, 'Transport', 'Pupil Arrears')
    rent = makeEmptyArrears('Tenant Arrears')
    driv = makeEmptyArrears('Student Arrears')
  if arrtype == 'driving':
    tran = makeEmptyArrears('Pupil Arrears')
    rent = makeEmptyArrears('Tenant Arrears')
    driv = preparrdata(Student, DrivingPay, 'Driving', 'Student Arrears')
  if arrtype == 'rent':
    tran = makeEmptyArrears('Pupil Arrears')
    rent = preparrdata(Tenant, RentPay, 'Rent', 'Tenant Arrears')
    driv = makeEmptyArrears('Student Arrears')
  data.append(tran)
  data.append(rent)
  data.append(driv)
  data.append(datetime.now().date())
  return data

def getPayDetails(obj, pay, typ):
  data = []
#  objPay = []
  print(typ, obj)
  data.append(obj)
  if typ == 'pup':
    objPay = pay.objects.filter(pupil=obj)
    arr = getTransportArrears(obj)
  elif typ == 'drv':
    objPay = pay.objects.filter(student=obj)
    arr = getDrivingArrears(obj)
  elif typ == 'rent':
    objPay = pay.objects.filter(tenant=obj)
    arr = getRentArrears(obj)
  if len(objPay) > 0:
    data.append(objPay)
  else: data.append('No payments received')
  data.append(arr)
  return data

def getPupilDetails(pupil):
  data = getPayDetails(pupil, TransportPay, 'pup')
  estpup = EstatePupil.objects.filter(pupil=pupil)
  if len(estpup) > 0:
    data.append(estpup)
  else: data.append([])
  trm = TermPupil.objects.filter(pupil=pupil)
  if len(trm) > 0:
    data.append(trm)
  else: data.append([])
  return data

def getStudentDetails(student):
  data = getPayDetails(student, DrivingPay, 'drv')
  cn=Attendance.objects.filter(student=student).values('lesson').annotate(cnt=Count('lesson'))
  data.append(len(cn))
  statt=StudentEnrolment.objects.filter(student=student)
  if len(statt)>0:
    data.append(statt)
  else: data.append([])
  return data

def getTenantDetails(tenant):
  data = getPayDetails(tenant, RentPay, 'rent')
  rmten = Room_Tenant.objects.filter(tenant=tenant)
  if len(rmten)>0:
    data.append(rmten)
  else: data.append([])
  return data

# View management snippets
def save_form(request, form, Model, page, urlroot, template):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            tmpl = 'includes/partial_list.html'
            objdata = get_data_list(request, Model, form, urlroot, page)
            data['html_list'] = render_to_string(tmpl, {'data': objdata})
        else:
            data['form_is_valid'] = False
    formdata = []
    formdata.append(page)
    formdata.append(form)
    context = {'formdata': formdata}
    data['html_form'] = render_to_string(template, context, request=request)
    return JsonResponse(data)

def create_form(request, Form):
    if request.method == 'POST':
        form = Form(request.POST)
    else:
        form = Form()
    return form

def update_form(request, pk, Form, Model):
    obj = get_object_or_404(Model, pk=pk)
    if request.method == 'POST':
        form = Form(request.POST, instance=obj)
    else:
        form = Form(instance=obj)
    return form

def delete_form(request, pk, Form, Model, url, urlroot):
    obj = get_object_or_404(Model, pk=pk)
    page = dict()
    data = dict()
    if request.method == 'POST':
        obj.delete()
        page = get_page(Model._meta.verbose_name, urlroot + '_create', Model._meta.verbose_name)
        data['form_is_valid'] = True
        tmpl = 'includes/partial_list.html'
        objdata = get_data_list(request, Model, Form, urlroot, page)
        data['html_list'] = render_to_string(tmpl, {'data': objdata})
    else:
        page['url'] = url
        page['objname'] = Model._meta.verbose_name
        page['objtitle'] = obj.__str__()
        formdata = []
        formdata.append(page)
        formdata.append(obj)
        context = {'formdata': formdata}
        tmpl = 'includes/partial_delete.html'
        data['html_form'] = render_to_string(tmpl, context, request=request)
    return data

#Term Object manipulation
def get_page(heading, create_url, new):
    page = dict()
    page['heading'] = heading
    page['create_url'] = reverse(create_url)
    page['new'] = new 
    return page

def obj_create(request, Form, Model, rev_url):
    form = create_form(request, Form)
    page = dict()
    page['url'] = reverse(rev_url)
    page['objname'] = Model._meta.verbose_name
    return form, page

def obj_update(request, pk, Form, Model, rev_url):
    form = update_form(request, pk, Form, Model)
    page = dict()
    page['url'] = reverse(rev_url, args={pk})
    page['objname'] = Model._meta.verbose_name
    return form, page

def pageddata(request, data, items):
    page = request.GET.get('page', 1)
    paginator = Paginator(data, items)
    try:
        pgdata = paginator.page(page)
    except PageNotAnInteger:
        pgdata = paginator.page(1)
    except EmptyPage:
        pgdata = paginator.page(paginator.num_pages)
    return pgdata

def get_data_list(request, Model, ModelForm, urlroot, pagedata):
    objects = Model.objects.all()
    fields = ModelForm._meta.fields
    data = []
    pk = Model._meta.pk.name
    create_url = urlroot + '_create'
    update_url = urlroot + '_update'
    delete_url = urlroot + '_delete'
    for obj in objects:
      row = dict()
      rowurl = dict()
      datapiece = []
      for fld in fields:
        row[obj._meta.get_field(fld).verbose_name] = getattr(obj, fld)
      rowurl['update'] = reverse(update_url, args={getattr(obj, pk)})
      rowurl['delete'] = reverse(delete_url, args={getattr(obj, pk)})
      datapiece.append(row)
      datapiece.append(rowurl)
      data.append(datapiece)
    pgdata = pageddata(request, data, 20)
    objdata = [] 
    objdata.append(pagedata)
    objdata.append(pgdata)
    return objdata

def add_formset(request, Form, Model, text, url):
  ModelFormset = formset_factory(Form, extra=5)
  fields = Form._meta.fields

  if request.method == "POST":
    formset = ModelFormset(request.POST, request.FILES)
    if formset.is_valid():
      for fm in formset:
        formdata = dict()
        valid_data = False 
        for fld in fields:
          formdata[fld] = fm.cleaned_data.get(fld)
          if fm.cleaned_data.get(fld): valid_data = True 
        if valid_data:
          fm.save()
  else:
      formset = ModelFormset()
  data = []
  data.append(text)
  data.append(formset)
  data.append(reverse(url))
  return data
