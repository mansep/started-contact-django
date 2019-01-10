from django import forms

class ProfileForm(forms.Form):
    
	first_name = forms.CharField(max_length=100, required=True)
	last_name = forms.CharField(max_length=100, required=True)
	phone = forms.CharField(max_length=20, required=False)
	picture = forms.ImageField()