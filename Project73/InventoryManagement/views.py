
from django.shortcuts import render,redirect
from .models import Product
from .forms import Productform
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required





def Homeview(request):
    template_name='Home.html'
    return render(request,template_name)

def Aboutview(request):
    template_name='About.html'
    return render(request,template_name)

@login_required
def Addproductview(request):
    form=Productform()
    if request.method == 'POST':
        form=Productform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('showproduct')
    template_name='addproduct.html'
    context={'form':form}
    return render(request,template_name,context)

@login_required
def Showproductview(request):
    prd=Product.objects.all()
    template_name='Showproduct.html'
    context={'prd':prd}
    return render(request,template_name,context)

@login_required
def Updateview(request,update):
    prd=Product.objects.get(id=update)
    form=Productform(instance=prd)
    if request.method == 'POST':
        form=Productform(request.POST,instance=prd)
        if form.is_valid():
            form.save()
            return redirect('showproduct')
    template_name='addproduct.html'
    context={'form':form}
    return render(request,template_name,context)

@login_required
def Deleteview(request,delete):
    prd=Product.objects.get(id=delete)
    prd.delete()
    return redirect('showproduct')

def Registeruserview(request):
    form=UserCreationForm()
    if request.method == 'POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    template_name='register.html'
    context={'form':form}
    return render(request,template_name,context)

def Loginuserview(request):
    if request.method == 'POST':
        u=request.POST.get('uname')
        p=request.POST.get('password')

        user=authenticate(username=u,password=p)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.error(request,'Invalid Cridential')
    template_name='login.html'
    return render(request,template_name)

def Logoutview(request):
    logout(request)
    return redirect('login')
