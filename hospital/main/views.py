# from django.shortcuts import render
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib import messages
# from django.http import HttpResponseRedirect

# def home(request):
#     return render(request,'main/home.html')

# def register(request):
#     form=UserCreationForm
#     if request.method=='POST':
#         regForm=UserCreationForm(request.POST)
#         if regForm.is_valid():
#             regForm.save()
#             messages.success(request,'User has been registered')
    
#     return render(request,'main/register.html',{'form':form})




from django.shortcuts import render, redirect 
from django.http import HttpResponse
# from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

from django.contrib.auth.decorators import login_required

# Create your views here.
from .models import *
from .forms import CreateUserForm
# from .filters import OrderFilter

def registerPage(request):
	# if request.user.is_authenticated:
	# 	return redirect('home')
	# else:
		form = CreateUserForm()
		if request.method == 'POST':
			form = CreateUserForm(request.POST)
			if form.is_valid():
				form.save()
				user = form.cleaned_data.get('username')
				messages.success(request, 'Account was created for ' + user)

				return redirect('login')
			

		context = {'form':form}
		return render(request, 'main/register.html', context)

def loginPage(request):
	# if (request.user.is_authenticated):
	# 	return redirect('home')
	# else:
		if request.method == 'POST':
			username = request.POST.get('username')
			password =request.POST.get('password')

			user = authenticate(request, username=username, password=password)

			if user is not None:
				login(request, user)
				return redirect('home')
			else:
				messages.info(request, 'Username OR password is incorrect')

		context = {}
		return render(request, 'main/login.html', context)

def logoutUser(request):
	logout(request)
	return redirect('login')

# @login_required(login_url='login')
def homepage(request):
	return render(request, 'main/homepage.html',)

def department(request):
	return render(request, 'main/department.html',)

@login_required(login_url='login')
def home(request):
	return render(request, 'main/home.html',)

@login_required(login_url='login')
def registerPage(request):
	# if request.user.is_authenticated:
	# 	return redirect('home')
	# else:
		form = CreateUserForm()
		if request.method == 'POST':
			form = CreateUserForm(request.POST)
			if form.is_valid():
				form.save()
				user = form.cleaned_data.get('username')
				messages.success(request, 'Account was created for ' + user)

				return redirect('login')
			

		context = {'form':form}
		return render(request, 'main/register.html', context)

def loginPage2(request):
	# if (request.user.is_authenticated):
	# 	return redirect('home')
	# else:
		if request.method == 'POST':
			username = request.POST.get('username')
			password =request.POST.get('password')

			user = authenticate(request, username=username, password=password)

			if user is not None:
				login(request, user)
				return redirect('register')
			else:
				messages.info(request, 'Username OR password is incorrect')

		context = {}
		return render(request, 'main/login2.html', context)

def logoutUser2(request):
	logout(request)
	return redirect('login2')