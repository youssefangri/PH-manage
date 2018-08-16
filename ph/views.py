from django.contrib.auth import authenticate, login, get_user_model
from django.shortcuts import render, redirect

from .forms import LoginFrom
from Medicament.models import Medicament

def home_page(request):
	queryset = Medicament.objects.all()
	content = {	
		"title":"pharmacie",
	}
	if request.user.is_authenticated():
		content["object_list"]= queryset
	return render(request, "home_page.html",content)

def login_page(request):
	form = LoginFrom(request.POST or None)
	content = {
		"Title":"Login Page",
		"form":form
	}
	
	if form.is_valid():
		print(form.cleaned_data)
		username = form.cleaned_data.get('username')
		password = form.cleaned_data.get('password')
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			#content['form']= LoginFrom()
			return redirect("/")
		else :
			print('Error')
		
	print(request.user.is_authenticated())
	return render(request,"auth/login.html",content)
	
User = get_user_model()
	
