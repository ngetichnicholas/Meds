from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from . import views as app_views
from django.contrib.auth import views as auth_views



urlpatterns = [
  path('admin/', admin.site.urls),
  path('', app_views.index, name="home"),
  path('accounts/login/',app_views.login,name='login'),
  path('logout/',auth_views.LogoutView.as_view(template_name = 'registration/logout.html'),name='logout'),
]