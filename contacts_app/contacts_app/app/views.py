# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from app.forms import UserForm, UserProfileInfoForm,ContactsInfoForm
from app.models import UserProfileInfo, ContactsInfo

# Create your views here.
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required

def index(request):  
    contact_form = ContactsInfoForm()	
    user_list = ContactsInfo.objects.filter(username=request.user.username)	 
    if request.method == "POST":
    	contact_form = ContactsInfoForm(data=request.POST)

    	if contact_form.is_valid():
    		cont = contact_form.save()
    		cont.username=request.user.username
    		cont.save()
    		return render(request,'app/index.html',{"contact_form":contact_form,"users":user_list})

    	


    	else:
    		print(contact_form.errors)
    		return render(request,'app/index.html',{"contact_form":contact_form,"users":user_list})


    else:
        		
    	return render(request,'app/index.html',{"contact_form":contact_form,"users":user_list})

def register(request):
	
	registered=False

	if request.method == "POST":

		user_form = UserForm(data=request.POST)
		profile_form = UserProfileInfoForm(data=request.POST)

		if user_form.is_valid() and profile_form.is_valid():
			user = user_form.save()
			user.set_password(user.password)
			user.save()
			profile = profile_form.save(commit=False)
			profile.user = user
			profile.save()

			registered = True
		else:
			print(user_form.errors,profile_form.errors)

	else:
		user_form = UserForm()
		profile_form = UserProfileInfoForm()

	 
	return render(request,'app/registration.html',{
		               'user_form':user_form,
		               'profile_form':profile_form,
		               'registered':registered}) 

def user_login(request):

	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')

		user = authenticate(username=username,password=password)

		if user:
			if user.is_active:
				login(request,user)

				return HttpResponseRedirect(reverse('index'))

			else:
				return HttpResponse("Your account is not active")

		else:
			print("someone tried to login and failed")
			return render(request,'app/login.html',{})	
	else:

		return render(request,'app/login.html',{})				


@login_required
def user_logout(request):
    # Log out the user.
    logout(request)
    # Return to homepage.
    return HttpResponseRedirect(reverse('index'))

    



