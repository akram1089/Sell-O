from django.contrib import admin
from django.urls import path,include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',views.home,name='home'),
    path('services',views.services,name='services'),
    path('about',views.about,name='about'),
    path('contact',views.contact,name='contact'),
    path('signup',views.signup,name='signup'),
    path('login_user',views.login_user,name='login_user'),
    path('log_out',views.log_out,name='log_out'),
    path('admin_login',views.admin_login,name='admin_login'),
    path('admin_log',views.admin_log,name='admin_log'),
    path('admin_logout',views.admin_logout,name='admin_logout'),
    path('upload_data',views.upload_data,name='upload_data'),
    path('view_data',views.view_data,name='view_data'),
    path('multidata_data_upload',views.multidata_data_upload,name='multidata_data_upload'),
    path('del_data<str:id>',views.del_data,name='del_data'),
    path('edit_data<str:id>',views.edit_data,name='edit_data'),
    path('Add_cart/<str:id>',views.Add_cart,name='Add_cart'),
    path('reset_password/',views.reset_password,name='reset_password'),
    path('change_pass/<token>/',views.change_pass,name='change_pass'),
   
]
from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)