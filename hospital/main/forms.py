# from django import forms

# # creating a form
# class InputForm(forms.Form):

# 	first_name = forms.CharField(max_length = 200)
# 	last_name = forms.CharField(max_length = 200)
# 	roll_number = forms.IntegerField(
# 					help_text = "Enter 6 digit roll number"
# 					)
# 	password = forms.CharField(widget = forms.PasswordInput())


from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms



# from .models import Order


class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']