from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import login as auth_login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from .forms import *



# Create your views here.
@login_required
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

def add_patient(request):
  if request.method == 'POST':
    add_patient_form = PatientForm(request.POST)
    if add_patient_form.is_valid():
      patient = add_patient_form.save(commit=False)
      patient.save()
      return redirect('home')

  else:
    add_patient_form = PatientForm()
    
  return render(request, 'add_patient.html',{'add_patient_form':add_patient_form})

def add_appointment(request):
  if request.method == 'POST':
    add_appointment_form = AppointmentForm(request.POST)
    if add_appointment_form.is_valid():
      appointment = add_appointment_form.save(commit=False)
      appointment.save()
      return redirect('home')

  else:
    add_appointment_form = AppointmentForm()
    
  return render(request, 'add_appointment.html',{'add_appointment_form':add_appointment_form})

def add_prescription(request):
  if request.method == 'POST':
    add_prescription_form = PrescriptionForm(request.POST)
    if add_prescription_form.is_valid():
      prescription = add_prescription_form.save(commit=False)
      prescription.save()
      return redirect('home')

  else:
    add_prescription_form = PrescriptionForm()
    
  return render(request, 'add_prescription.html',{'add_prescription_form':add_prescription_form})

def add_drug(request):
  if request.method == 'POST':
    add_drug_form = DrugForm(request.POST)
    if add_drug_form.is_valid():
      drug = add_drug_form.save(commit=False)
      drug.save()
      return redirect('home')

  else:
    add_drug_form = DrugForm()
    
  return render(request, 'add_drug.html',{'add_drug_form':add_drug_form})

def add_feedback(request):
  if request.method == 'POST':
    add_feedback_form = FeedbackForm(request.POST)
    if add_feedback_form.is_valid():
      feedback = add_feedback_form.save(commit=False)
      feedback.save()
      return redirect('home')

  else:
    add_feedback_form = FeedbackForm()
    
  return render(request, 'add_feedback.html',{'add_feedback_form':add_feedback_form})

def add_health_history(request):
  if request.method == 'POST':
    add_history_form = HealthHistoryForm(request.POST)
    if add_history_form.is_valid():
      history = add_history_form.save(commit=False)
      history.save()
      return redirect('home')

  else:
    add_history_form = HealthHistoryForm()
    
  return render(request, 'add_health_history.html',{'add_history_form':add_history_form})

def visits(request,patient_id):
  visits = Visit.objects.filter(patient_id = patient_id).order_by('-date_visited')
  return render(request,'visits.html',{'visits':visits})

def add_visit(request):
  if request.method == 'POST':
    add_visit_form = VisitForm(request.POST)
    if add_visit_form.is_valid():
      visit = add_visit_form.save(commit=False)
      visit.save()
      return redirect('home')

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
      return redirect('home')
  else:
    update_visit_form = VisitForm(instance=visit)

  return render(request, 'update_visit.html', {"update_visit_form":update_visit_form})


