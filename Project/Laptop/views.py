from django import forms
from django.core import paginator
from django.shortcuts import redirect, render
from .forms import LaptopModelForm
from .models import Laptop
from django.core.paginator import Paginator


# Create your views here.

def LaptopRegister_view(request):
    form=LaptopModelForm()
    if request.method=='POST':
        form=LaptopModelForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('lapShow')
    template_name='Laptop/LaptopRegister.html'
    context={'form':form}
    return render(request,template_name,context)

def LaptopShow_view(request):
    lap=Laptop.objects.all()
    paginator=Paginator(lap,1)
    page_number=request.GET.get('page')
    page_obj=paginator.get_page(page_number)
    template_name='Laptop/LaptopShow.html'
    context={'page_obj': page_obj}
    # context={'lap':lap}
    return render(request,template_name,context)
