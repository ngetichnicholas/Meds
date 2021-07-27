from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import login as auth_login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate



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

