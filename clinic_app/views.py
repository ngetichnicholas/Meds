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
    add_patient_form = AddPatientForm(request.POST)
    if add_patient_form.is_valid():
      patient = add_patient_form.save(commit=False)
      patient.save()
      return redirect('home')

  else:
    add_patient_form = AddPatientForm()
    
  return render(request, 'add_patient.html',{'add_patient_form':add_patient_form})

def add_appointment(request):
  if request.method == 'POST':
    add_appointment_form = AddAppointmentForm(request.POST)
    if add_appointment_form.is_valid():
      patient = add_appointment_form.save(commit=False)
      patient.save()
      return redirect('home')

  else:
    add_appointment_form = AddAppointmentForm()
    
  return render(request, 'add_appointment.html',{'add_appointment_form':add_appointment_form})

def add_prescription(request):
  if request.method == 'POST':
    add_prescription_form = AddPrescriptionForm(request.POST)
    if add_prescription_form.is_valid():
      patient = add_prescription_form.save(commit=False)
      patient.save()
      return redirect('home')

  else:
    add_prescription_form = AddPrescriptionForm()
    
  return render(request, 'add_prescription.html',{'add_prescription_form':add_prescription_form})

def add_drug(request):
  if request.method == 'POST':
    add_drug_form = AddDrugForm(request.POST)
    if add_drug_form.is_valid():
      patient = add_drug_form.save(commit=False)
      patient.save()
      return redirect('home')

  else:
    add_drug_form = AddDrugForm()
    
  return render(request, 'add_drug.html',{'add_drug_form':add_drug_form})

