from django import forms
from django.contrib.auth import get_user_model

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

