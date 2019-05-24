from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from fayvad.general import *
from .models import *
from .forms import *

# Class Object
def get_class_list(request):
    page = get_page('Classes', 'driving:class_create', 'Class')
    data = get_data_list(request,Class, ClassForm, 'driving:class', page)
    return data

@login_required
def class_list(request):
    data = get_class_list(request)
    return render(request, 'list.html', {'data': data})

@login_required
def class_create(request):
    form, page = obj_create(request, ClassForm, Class, 'driving:class_create')
    return save_form(request, form, Class, page, 'driving:class', 'includes/partial_create.html')

@login_required
def class_update(request, pk):
    form, page = obj_update(request, pk, ClassForm, Class, 'driving:class_update')
    return save_form(request, form, Class, page, 'driving:class', 'includes/partial_update.html')

@login_required
def class_delete(request, pk):
    url = reverse('driving:class_delete', args={pk})
    data = delete_form(request, pk, ClassForm, Class, url, 'driving:class',)
    return JsonResponse(data)

# Branch Object
def get_branch_list(request):
    page = get_page('Branches', 'driving:branch_create', 'Branch')
    data = get_data_list(request,Branch, BranchForm, 'driving:branch', page)
    return data

@login_required
def branch_list(request):
    data = get_branch_list(request)
    return render(request, 'list.html', {'data': data})

@login_required
def branch_create(request):
    form, page = obj_create(request, BranchForm, Branch, 'driving:branch_create')
    return save_form(request, form, Branch, page, 'driving:branch', 'includes/partial_create.html')

@login_required
def branch_update(request, pk):
    form, page = obj_update(request, pk, BranchForm, Branch, 'driving:branch_update')
    return save_form(request, form, Branch, page, 'driving:branch', 'includes/partial_update.html')

@login_required
def branch_delete(request, pk):
    url = reverse('driving:branch_delete', args={pk})
    data = delete_form(request, pk, BranchForm, Branch, url, 'driving:branch',)
    return JsonResponse(data)

# Student Enrolment Object
def get_stud_enrol_list(request):
    page = get_page('Students Enrolment', 'driving:stud_enrol_create', 'Student Enrolment')
    data = get_data_list(request,StudentEnrolment, StudentEnrolmentForm, 'driving:stud_enrol', page)
    return data

@login_required
def stud_enrol_list(request):
    data = get_stud_enrol_list(request)
    return render(request, 'list.html', {'data': data})

@login_required
def stud_enrol_create(request):
    form, page = obj_create(request, StudentEnrolmentForm, StudentEnrolment, 'driving:stud_enrol_create')
    return save_form(request, form, StudentEnrolment, page, 'driving:stud_enrol', 'includes/partial_create.html')

@login_required
def stud_enrol_update(request, pk):
    form, page = obj_update(request, pk, StudentEnrolmentForm, StudentEnrolment, 'driving:stud_enrol_update')
    return save_form(request, form, StudentEnrolment, page, 'driving:stud_enrol', 'includes/partial_update.html')

@login_required
def stud_enrol_delete(request, pk):
    url = reverse('driving:stud_enrol_delete', args={pk})
    data = delete_form(request, pk, StudentEnrolmentForm, StudentEnrolment, url, 'driving:stud_enrol',)
    return JsonResponse(data)

# Tutor Object
def get_tutor_list(request):
    page = get_page('Tutors', 'driving:tutor_create', 'Tutor')
    data = get_data_list(request,Tutor, TutorForm, 'driving:tutor', page)
    return data

@login_required
def tutor_list(request):
    data = get_tutor_list(request)
    return render(request, 'list.html', {'data': data})

@login_required
def tutor_create(request):
    form, page = obj_create(request, TutorForm, Tutor, 'driving:tutor_create')
    return save_form(request, form, Tutor, page, 'driving:tutor', 'includes/partial_create.html')

@login_required
def tutor_update(request, pk):
    form, page = obj_update(request, pk, TutorForm, Tutor, 'driving:tutor_update')
    return save_form(request, form, Tutor, page, 'driving:tutor', 'includes/partial_update.html')

@login_required
def tutor_delete(request, pk):
    url = reverse('driving:tutor_delete', args={pk})
    data = delete_form(request, pk, TutorForm, Tutor, url, 'driving:tutor',)
    return JsonResponse(data)

# Student Object
def get_student_list(request):
    page = get_page('Students', 'driving:student_create', 'Student')
    data = get_data_list(request,Student, StudentForm, 'driving:student', page)
    return data

@login_required
def student_list(request):
    data = get_student_list(request)
    return render(request, 'list.html', {'data': data})

@login_required
def student_create(request):
    form, page = obj_create(request, StudentForm, Student, 'driving:student_create')
    return save_form(request, form, Student, page, 'driving:student', 'includes/partial_create.html')

@login_required
def student_update(request, pk):
    form, page = obj_update(request, pk, StudentForm, Student, 'driving:student_update')
    return save_form(request, form, Student, page, 'driving:student', 'includes/partial_update.html')

@login_required
def student_delete(request, pk):
    url = reverse('driving:student_delete', args={pk})
    data = delete_form(request, pk, StudentForm, Student, url, 'driving:student',)
    return JsonResponse(data)

# ExamBooking Object
def get_exambooking_list(request):
    page = get_page('Exam Bookings', 'driving:exambooking_create', 'Exam Booking')
    data = get_data_list(request,ExamBooking, ExamBookingForm, 'driving:exambooking', page)
    return data

@login_required
def exambooking_list(request):
    data = get_exambooking_list(request)
    return render(request, 'list.html', {'data': data})

@login_required
def exambooking_create(request):
    form, page = obj_create(request, ExamBookingForm, ExamBooking, 'driving:exambooking_create')
    return save_form(request, form, ExamBooking, page, 'driving:exambooking', 'includes/partial_create.html')

@login_required
def exambooking_update(request, pk):
    form, page = obj_update(request, pk, ExamBookingForm, ExamBooking, 'driving:exambooking_update')
    return save_form(request, form, ExamBooking, page, 'driving:exambooking', 'includes/partial_update.html')

@login_required
def exambooking_delete(request, pk):
    url = reverse('driving:exambooking_delete', args={pk})
    data = delete_form(request, pk, ExamBookingForm, ExamBooking, url, 'driving:exambooking',)
    return JsonResponse(data)

# Period Object
def get_period_list(request):
    page = get_page('Periods', 'driving:period_create', 'Period')
    data = get_data_list(request,Period, PeriodForm, 'driving:period', page)
    return data

@login_required
def period_list(request):
    data = get_period_list(request)
    return render(request, 'list.html', {'data': data})

@login_required
def period_create(request):
    form, page = obj_create(request, PeriodForm, Period, 'driving:period_create')
    return save_form(request, form, Period, page, 'driving:period', 'includes/partial_create.html')

@login_required
def period_update(request, pk):
    form, page = obj_update(request, pk, PeriodForm, Period, 'driving:period_update')
    return save_form(request, form, Period, page, 'driving:period', 'includes/partial_update.html')

@login_required
def period_delete(request, pk):
    url = reverse('driving:period_delete', args={pk})
    data = delete_form(request, pk, PeriodForm, Period, url, 'driving:period',)
    return JsonResponse(data)

# Rate Object
def get_rate_list(request):
    page = get_page('Rates', 'driving:rate_create', 'Rate')
    data = get_data_list(request,Rate, RateForm, 'driving:rate', page)
    return data

@login_required
def rate_list(request):
    data = get_rate_list(request)
    return render(request, 'list.html', {'data': data})

@login_required
def rate_create(request):
    form, page = obj_create(request, RateForm, Rate, 'driving:rate_create')
    return save_form(request, form, Rate, page, 'driving:rate', 'includes/partial_create.html')

@login_required
def rate_update(request, pk):
    form, page = obj_update(request, pk, RateForm, Rate, 'driving:rate_update')
    return save_form(request, form, Rate, page, 'driving:rate', 'includes/partial_update.html')

@login_required
def rate_delete(request, pk):
    url = reverse('driving:rate_delete', args={pk})
    data = delete_form(request, pk, RateForm, Rate, url, 'driving:rate',)
    return JsonResponse(data)

# Attendance Object
def get_attendance_list(request):
    page = get_page('Class Attendance', 'driving:attendance_create', 'Class Attendace')
    data = get_data_list(request, Attendance, AttendanceForm, 'driving:attendance', page)
    return data

@login_required
def attendance_list(request):
    data = get_attendance_list(request)
    return render(request, 'list.html', {'data': data})

@login_required
def attendance_create(request):
    form, page = obj_create(request, AttendanceForm, Attendance, 'driving:attendance_create')
    return save_form(request, form, Attendance, page, 'driving:attendance', 'includes/partial_create.html')

@login_required
def attendance_update(request, pk):
    form, page = obj_update(request, pk, AttendanceForm, Attendance, 'driving:attendance_update')
    return save_form(request, form, Attendance, page, 'driving:attendance', 'includes/partial_update.html')

@login_required
def attendance_delete(request, pk):
    url = reverse('driving:attendance_delete', args={pk})
    data = delete_form(request, pk, AttendanceForm, Attendance, url, 'driving:attendance',)
    return JsonResponse(data)

# Payment Object
def get_payment_list(request):
    page = get_page('Payments', 'driving:payment_create', 'Payment')
    data = get_data_list(request,Payment, PaymentForm, 'driving:payment', page)
    return data

@login_required
def payment_list(request):
    data = get_payment_list(request)
    return render(request, 'list.html', {'data': data})

@login_required
def payment_create(request):
    form, page = obj_create(request, PaymentForm, Payment, 'driving:payment_create')
    return save_form(request, form, Payment, page, 'driving:payment', 'includes/partial_create.html')

@login_required
def payment_update(request, pk):
    form, page = obj_update(request, pk, PaymentForm, Payment, 'driving:payment_update')
    return save_form(request, form, Payment, page, 'driving:payment', 'includes/partial_update.html')

@login_required
def payment_delete(request, pk):
    url = reverse('driving:payment_delete', args={pk})
    data = delete_form(request, pk, PaymentForm, Payment, url, 'driving:payment',)
    return JsonResponse(data)

# License Object
def get_license_list(request):
    page = get_page('Licenses', 'driving:license_create', 'License')
    data = get_data_list(request,License, LicenseForm, 'driving:license', page)
    return data

@login_required
def license_list(request):
    data = get_license_list(request)
    return render(request, 'list.html', {'data': data})

@login_required
def license_create(request):
    form, page = obj_create(request, LicenseForm, License, 'driving:license_create')
    return save_form(request, form, License, page, 'driving:license', 'includes/partial_create.html')

@login_required
def license_update(request, pk):
    form, page = obj_update(request, pk, LicenseForm, License, 'driving:license_update')
    return save_form(request, form, License, page, 'driving:license', 'includes/partial_update.html')

@login_required
def license_delete(request, pk):
    url = reverse('driving:license_delete', args={pk})
    data = delete_form(request, pk, LicenseForm, License, url, 'driving:license',)
    return JsonResponse(data)

# Discharge Object
def get_discharge_list(request):
    page = get_page('Discharges', 'driving:discharge_create', 'Discharge')
    data = get_data_list(request,Discharge, DischargeForm, 'driving:discharge', page)
    return data

@login_required
def discharge_list(request):
    data = get_discharge_list(request)
    return render(request, 'list.html', {'data': data})

@login_required
def discharge_create(request):
    form, page = obj_create(request, DischargeForm, Discharge, 'driving:discharge_create')
    return save_form(request, form, Discharge, page, 'driving:discharge', 'includes/partial_create.html')

@login_required
def discharge_update(request, pk):
    form, page = obj_update(request, pk, DischargeForm, Discharge, 'driving:discharge_update')
    return save_form(request, form, Discharge, page, 'driving:discharge', 'includes/partial_update.html')

@login_required
def discharge_delete(request, pk):
    url = reverse('driving:discharge_delete', args={pk})
    data = delete_form(request, pk, DischargeForm, Discharge, url, 'driving:discharge',)
    return JsonResponse(data)

@login_required
def add_exam_bookings(request):
  formset = add_formset(request, ExamBookingForm, ExamBooking, 'Exam Bookings', 'driving:add_exam_bookings') 
  return render(request, 'multiple.html', {'formset': formset})

@login_required
def add_rates(request):
  formset = add_formset(request, RateForm, Rate, 'Rates', 'driving:add_rates') 
  return render(request, 'multiple.html', {'formset': formset})

@login_required
def add_attendance(request):
  formset = add_formset(request, AttendanceForm, Attendance, 'Class Attendance', 'driving:add_attendance') 
  return render(request, 'multiple.html', {'formset': formset})

@login_required
def add_payments(request):
  formset = add_formset(request, PaymentForm, Payment, 'Payments', 'driving:add_payments') 
  return render(request, 'multiple.html', {'formset': formset})

@login_required
def add_licenses(request):
  formset = add_formset(request, LicenseForm, License, 'Licenses', 'driving:add_licenses') 
  return render(request, 'multiple.html', {'formset': formset})

@login_required
def add_discharges(request):
  formset = add_formset(request, DischargeForm, Discharge, 'Discharges', 'driving:add_discharges') 
  return render(request, 'multiple.html', {'formset': formset})

@login_required
def getstudentdetails(request, student):
  stud = student.split(' ')
  st = Student.objects.filter(fname=stud[0], lname=stud[1])[0]
  data = getStudentDetails(st)
  print (data)
  context = {'data': data}
  return render(request,'studentdetails.html', context)
