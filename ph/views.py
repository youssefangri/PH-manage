from django.contrib.auth import authenticate, login, get_user_model
from django.shortcuts import render, redirect


from .forms import LoginFrom, BuyForm
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


def buy_page(request):
	form = BuyForm(request.POST or None)
	content = {
		"Title":"Buy Page",
		"form":form
	}
	
	if form.is_valid():
		selected_Medicament = form.cleaned_data.get("Medicament")
		selected_Quantity = form.cleaned_data.get("Quantity")
		try:
			M = Medicament.objects.get(title=selected_Medicament)
			M.quantity = (M.quantity)-(selected_Quantity)	
			M.save()
			content["status"]="secceful"
		except:
			content["status"]="error"
			pass
	return render(request,"oper/buy.html",content)	
	
User = get_user_model()
	
