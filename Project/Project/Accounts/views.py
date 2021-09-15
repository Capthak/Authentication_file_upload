from django.shortcuts import render,redirect
from .forms import RegisterForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.core.mail import send_mail

# Create your views here.

def Regiter_view(request):
    form=RegisterForm()
    if request.method=="POST":
        form=RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            emil=form.cleaned_data['email']
            user=form.cleaned_data['username']
            subject='REGISTRATION'
            admin='noobpathak8@gmail.com'
            msg=f'Hello {user} ,Wellcome...To login click:http://127.0.0.1:8000/aut/login/'
            send_mail(subject,msg,admin,[emil],fail_silently=True)
            return redirect('LOGIN')
    template_name='Accounts/Register.html'
    context={'form':form}
    return render(request,template_name,context)

def login_view(request):
    if request.method=='POST':
        u=request.POST.get('uname')
        p=request.POST.get('pword')
        user=authenticate(username=u,password=p)
        if user:
            login(request,user)
            return redirect('home')
        messages.error(request,'Invalid Cred')
    template_name='Accounts/login.html'
    context={}
    return render(request,template_name,context)

def logout_view(request):
    logout(request)
    return redirect('LOGIN')

def changepass_view(request):
    if request.method=='POST':
        u=request.POST.get('uname')
        p=request.POST.get('pword')
        new=request.POST.get('new_pword')
        con=request.POST.get('con_pword')
        user=authenticate(username=u,password=p)
        if user  and new==con:
            usr=User.objects.get(username=u)
            co=str(con)
            usr.set_password(co)
            usr.save()
            return redirect('LOGIN')
        else:
            messages.error(request,'PlEASE enter corect credentials')
    template_name="Accounts/Change.html"
    context={}
    return render(request,template_name,context)

def home_view(request):
    return render(request,'Accounts/Home.html')



    



        