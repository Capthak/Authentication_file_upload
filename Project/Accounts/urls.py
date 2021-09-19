from django.urls import path
from .views import Regiter_view,login_view
from .views import logout_view,changepass_view,home_view
from django.contrib.auth.views import PasswordResetView,PasswordResetDoneView,PasswordResetConfirmView,PasswordResetCompleteView


urlpatterns=[
    path('home/',home_view,name='home'),
    path('register/',Regiter_view,name='register'),
    path('login/',login_view,name='LOGIN'),
    path('logout/',logout_view,name='LOGOUT'),
    path('change/',changepass_view,name="CHANGE"),
    path('password_reset/',PasswordResetView.as_view(),name='password_reset'),
    path('password_reset/done/',PasswordResetDoneView.as_view(),name='password_reset_done'),
    path('reset/<uidb64>/<token>/',PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
    path('reset/done',PasswordResetCompleteView.as_view(),name='password_reset_complete'),

]