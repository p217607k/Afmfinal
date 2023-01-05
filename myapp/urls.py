from django.urls import path,include
from django.conf import settings
from . import views
from . views import *

from .views import  UserDetailAPI,RegisterUserAPIView



from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from myapp.views import  LogoutView

urlpatterns = [
    
    path('logout/', LogoutView.as_view(), name='auth_logout'),
    path('' , views.index,),
    path('api/register/',RegisterUserAPIView.as_view()),
    # path('exl/',Exlfiledownload.as_view()),

    
    path('getpostalldevices/',alldevice.as_view(),name='token_obtain_pair'),
    
    # path('signup/',views.sign,name='signup_page'),
    path('login/',views.login,name='login_page'),
    path('accounts/',include('django.contrib.auth.urls')),
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name="password_reset.html"),name='reset_password'),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name="password_reset_sent.html"), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="password_reset_form.html"), name='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name="password_reset_done.html"), name='password_reset_complete'),
]