from django.http import response
from django.http.response import Http404, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import login as auth_login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from django.core.exceptions import ObjectDoesNotExist
from .forms import *
from .models import *
import datetime
import csv


# Create your views here.
def index(request):
  current_user = request.user
  return render(request, 'index.html',{'current_user':current_user})

def login(request):
  if request.method == 'POST':
    form = AuthenticationForm(request=request, data=request.POST)
    if form.is_valid():
      username = form.cleaned_data.get('username')
      password = form.cleaned_data.get('password')
      user = authenticate(username=username, password=password)
      if user is not None:
        auth_login(request, user)
        messages.info(request, f"You are now logged in as {username}")
        return redirect('home')
      else:
        messages.error(request, "Invalid username or password.")
    else:
      messages.error(request, "Invalid username or password.")
  form = AuthenticationForm()
  return render(request = request,template_name = "registration/login.html",context={"form":form})


#Patient views
def patients(request):
  patients = Patient.objects.all().order_by('-first_name')
  return render(request,'patients.html',{'patients':patients})

#Export  table data as csv
def export_patients(request):
  response = HttpResponse(content_type = 'text/csv')
  response['Content-Disposition'] = 'attachment; filename = Patients'+ str(datetime.datetime.now())+'.csv'

  writer = csv.writer(response)
  writer.writerow(['First Name','Last Name','ID Number','Birth certificate No','Gender','Age','Tel No'])

  patients = Patient.objects.all()

  for patient in patients:
    writer.writerow([patient.first_name,patient.last_name,patient.id_number,patient.birth_certificate_no,patient.gender,patient.age,patient.phone])

  return response

#Get single patient
def patient_details(request,patient_id):
  try:
    patient =get_object_or_404(Patient, pk = patient_id)

  except ObjectDoesNotExist:
    raise Http404()

  return render(request,'patient_details.html',{'patient':patient})

@login_required
def add_patient(request):
  if request.method == 'POST':
    add_patient_form = PatientForm(request.POST)
    if add_patient_form.is_valid():
      patient = add_patient_form.save(commit=False)
      patient.save()
      return redirect('patients')

  else:
    add_patient_form = PatientForm()
    
  return render(request, 'add_patient.html',{'add_patient_form':add_patient_form})

@login_required
def update_patient(request, patient_id):
  patient = Patient.objects.get(pk=patient_id)
  if request.method == 'POST':
    update_patient_form = PatientForm(request.POST,request.FILES, instance=patient)
    if update_patient_form.is_valid():
      update_patient_form.save()
      messages.success(request, f'Patient updated!')
      return redirect('patients')
  else:
    update_patient_form = PatientForm(instance=patient)

  return render(request, 'update_patient.html', {"update_patient_form":update_patient_form})

@login_required
def delete_patient(request,patient_id):
  patient = Patient.objects.get(pk=patient_id)
  if patient:
    patient.delete_patient()
  return redirect('patients')


#Appointment views
def appointments(request):
  appointments = PatientAppointment.objects.all().order_by('-date_made')
  return render(request,'appointments.html',{'appointments':appointments})

#Export  table data as csv
def export_appointments(request):
  response = HttpResponse(content_type = 'text/csv')
  response['Content-Disposition'] = 'attachment; filename = appointments'+ str(datetime.datetime.now())+'.csv'

  writer = csv.writer(response)
  writer.writerow(['First Name','Last Name','Gender','Age','Tel No','Status','Date Recorded','Appointment Date',])

  appointments = PatientAppointment.objects.all()

  for appointment in appointments:
    writer.writerow([appointment.first_name,appointment.last_name,appointment.gender,appointment.age,appointment.phone,appointment.approve,appointment.approve,appointment.date_made,appointment.appointment_date])

  return response

#Get single appointment
def appointment_details(request,appointment_id):
  try:
    appointment =get_object_or_404(PatientAppointment, pk = appointment_id)

  except ObjectDoesNotExist:
    raise Http404()

  return render(request,'appointment_details.html',{'appointment':appointment})

@login_required
def add_appointment(request):
  if request.method == 'POST':
    add_appointment_form = AppointmentForm(request.POST)
    if add_appointment_form.is_valid():
      appointment = add_appointment_form.save(commit=False)
      appointment.save()
      return redirect('appointments')

  else:
    add_appointment_form = AppointmentForm()
    
  return render(request, 'add_appointment.html',{'add_appointment_form':add_appointment_form})

@login_required
def update_appointment(request, appointment_id):
  appointment = PatientAppointment.objects.get(pk=appointment_id)
  if request.method == 'POST':
    update_appointment_form = AppointmentForm(request.POST,request.FILES, instance=appointment)
    if update_appointment_form.is_valid():
      update_appointment_form.save()
      messages.success(request, f'Appointment updated!')
      return redirect('appointments')
  else:
    update_appointment_form = AppointmentForm(instance=appointment)

  return render(request, 'update_appointment.html', {"update_appointment_form":update_appointment_form})

@login_required
def delete_appointment(request,appointment_id):
  appointment = PatientAppointment.objects.get(pk=appointment_id)
  if appointment:
    appointment.delete_patient_appointment()
  return redirect('appointments')


#Prescription views
def prescriptions(request):
  prescriptions = Prescription.objects.all().order_by('-date')
  return render(request,'prescriptions.html',{'prescriptions':prescriptions})

#Get single prescription
def prescription_details(request,prescription_id):
  try:
    prescription =get_object_or_404(Prescription, pk = prescription_id)

  except ObjectDoesNotExist:
    raise Http404()

  return render(request,'prescription_details.html',{'prescription':prescription})

@login_required
def add_prescription(request):
  if request.method == 'POST':
    add_prescription_form = PrescriptionForm(request.POST)
    if add_prescription_form.is_valid():
      prescription = add_prescription_form.save(commit=False)
      prescription.save()
      return redirect('prescriptions')

  else:
    add_prescription_form = PrescriptionForm()
    
  return render(request, 'add_prescription.html',{'add_prescription_form':add_prescription_form})

@login_required
def update_prescription(request, prescription_id):
  prescription = Prescription.objects.get(pk=prescription_id)
  if request.method == 'POST':
    update_prescription_form = PrescriptionForm(request.POST,request.FILES, instance=prescription)
    if update_prescription_form.is_valid():
      update_prescription_form.save()
      messages.success(request, f'Prescription updated!')
      return redirect('prescriptions')
  else:
    update_prescription_form = PrescriptionForm(instance=prescription)

  return render(request, 'update_prescription.html', {"update_prescription_form":update_prescription_form})

@login_required
def delete_prescription(request,prescription_id):
  prescription = Prescription.objects.get(pk=prescription_id)
  if prescription:
    prescription.delete_prescription()
  return redirect('prescriptions')


#Medicine views
def drugs(request):
  drugs = Medicine.objects.all()
  return render(request,'drugs.html',{'drugs':drugs})

#Get single drug
def drug_details(request,drug_id):
  try:
    drug =get_object_or_404(Medicine, pk = drug_id)

  except ObjectDoesNotExist:
    raise Http404()

  return render(request,'drug_details.html',{'drug':drug})

@login_required
def add_drug(request):
  if request.method == 'POST':
    add_drug_form = DrugForm(request.POST)
    if add_drug_form.is_valid():
      drug = add_drug_form.save(commit=False)
      drug.save()
      return redirect('drugs')

  else:
    add_drug_form = DrugForm()
    
  return render(request, 'add_drug.html',{'add_drug_form':add_drug_form})

@login_required
def update_drug(request, drug_id):
  drug = Medicine.objects.get(pk=drug_id)
  if request.method == 'POST':
    update_drug_form = DrugForm(request.POST,request.FILES, instance=drug)
    if update_drug_form.is_valid():
      update_drug_form.save()
      messages.success(request, f'Drug updated!')
      return redirect('drugs')
  else:
    update_drug_form = DrugForm(instance=drug)

  return render(request, 'update_drug.html', {"update_drug_form":update_drug_form})

@login_required
def delete_drug(request,drug_id):
  drug = Medicine.objects.get(pk=drug_id)
  if drug:
    drug.delete_medicine()
  return redirect('drugs')


#Feedback Views
def feedback(request):
  feedbacks = FeedBack.objects.all().order_by('-feedback_date')
  return render(request,'feedback.html',{'feedbacks':feedbacks})

#Get single feedback
def feedback_details(request,feedback_id):
  try:
    feedback =get_object_or_404(FeedBack, pk = feedback_id)

  except ObjectDoesNotExist:
    raise Http404()

  return render(request,'feedback_details.html',{'feedback':feedback})

@login_required
def add_feedback(request):
  if request.method == 'POST':
    add_feedback_form = FeedbackForm(request.POST)
    if add_feedback_form.is_valid():
      feedback = add_feedback_form.save(commit=False)
      feedback.save()
      return redirect('feedback')

  else:
    add_feedback_form = FeedbackForm()
    
  return render(request, 'add_feedback.html',{'add_feedback_form':add_feedback_form})

@login_required
def update_feedback(request, feedback_id):
  feedback = FeedBack.objects.get(pk=feedback_id)
  if request.method == 'POST':
    update_feedback_form = FeedbackForm(request.POST,request.FILES, instance=feedback)
    if update_feedback_form.is_valid():
      update_feedback_form.save()
      messages.success(request, f'Feedback updated!')
      return redirect('feedback')
  else:
    update_feedback_form = FeedbackForm(instance=feedback)

  return render(request, 'update_feedback.html', {"update_feedback_form":update_feedback_form})

@login_required
def delete_feedback(request,feedback_id):
  feedback = FeedBack.objects.get(pk=feedback_id)
  if feedback:
    feedback.delete_feedback()
  return redirect('feedback')

#Health History views
def history(request):
  histories = PatientHealthHistory.objects.all().order_by('-date_recorded')
  return render(request,'history.html',{'histories':histories})

#Get single history
def history_details(request,history_id):
  try:
    history =get_object_or_404(PatientHealthHistory, pk = history_id)

  except ObjectDoesNotExist:
    raise Http404()

  return render(request,'history_details.html',{'history':history})

def add_health_history(request):
  if request.method == 'POST':
    add_history_form = HealthHistoryForm(request.POST)
    if add_history_form.is_valid():
      history = add_history_form.save(commit=False)
      history.save()
      return redirect('history')

  else:
    add_history_form = HealthHistoryForm()
    
  return render(request, 'add_health_history.html',{'add_history_form':add_history_form})

@login_required
def update_history(request, history_id):
  history = PatientHealthHistory.objects.get(pk=history_id)
  if request.method == 'POST':
    update_history_form = HealthHistoryForm(request.POST,request.FILES, instance=history)
    if update_history_form.is_valid():
      update_history_form.save()
      messages.success(request, f'Health history updated!')
      return redirect('history')
  else:
    update_history_form = HealthHistoryForm(instance=history)

  return render(request, 'update_history.html', {"update_history_form":update_history_form})

@login_required
def delete_history(request,history_id):
  history = PatientHealthHistory.objects.get(pk=history_id)
  if history:
    history.delete_patient_health_history()
  return redirect('history')


#Patient Visits views
def visits(request):
  visits = Visit.objects.all().order_by('-date_visited')
  return render(request,'visits.html',{'visits':visits})

#Get single visit
def visit_details(request,visit_id):
  try:
    visit =get_object_or_404(Visit, pk = visit_id)

  except ObjectDoesNotExist:
    raise Http404()

  return render(request,'visit_details.html',{'visit':visit})

@login_required
def add_visit(request):
  if request.method == 'POST':
    add_visit_form = VisitForm(request.POST)
    if add_visit_form.is_valid():
      visit = add_visit_form.save(commit=False)
      visit.save()
      return redirect('visits')

  else:
    add_visit_form = VisitForm()
    
  return render(request, 'add_visit.html',{'add_visit_form':add_visit_form})


@login_required
def update_visit(request, visit_id):
  visit = Visit.objects.get(pk=visit_id)
  if request.method == 'POST':
    update_visit_form = VisitForm(request.POST,request.FILES, instance=visit)
    if update_visit_form.is_valid():
      update_visit_form.save()
      messages.success(request, f'Visit updated!')
      return redirect('visits')
  else:
    update_visit_form = VisitForm(instance=visit)

  return render(request, 'update_visit.html', {"update_visit_form":update_visit_form})

@login_required
def delete_visit(request,visit_id):
  visit = Visit.objects.get(pk=visit_id)
  if visit:
    visit.delete_visit()
  return redirect('visits')