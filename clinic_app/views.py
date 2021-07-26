from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def index(request):
  current_user = request.user
  return render(request, 'index.html',{'current_user':current_user})
