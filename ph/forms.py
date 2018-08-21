from django import forms
from django.contrib.auth import get_user_model

from Medicament.models import Medicament

class LoginFrom(forms.Form):
	
	username = forms.CharField(
								
			widget= forms.TextInput(
										attrs={
										"class":"form-control",
										"id":"username",
										"placeholder":"Username",
												}
									)
								)
			
			
	password = forms.CharField(
	
			widget = forms.PasswordInput(
			
										attrs={
										"class":"form-control",
										"id":"password",
										"placeholder":"Password"
											}
										)	
								)
								
User = get_user_model()

class BuyForm(forms.Form):
	Medicament = forms.CharField(widget= forms.TextInput(
										attrs={
										"class":"form-control",
										"id":"Medicament",
										"placeholder":"Medicament",
												}
									))
	Quantity = forms.IntegerField(widget= forms.TextInput(
										attrs={
										"class":"form-control",
										"id":"Quantity",
										"placeholder":"Quantity",
												}
									))
	def clean_Medicament(self):
		if Medicament.DoesNotExist:
			raise forms.ValidationError("Medicament not exist")
		return 

