from django import forms

class ProfileForm(forms.Form):
    
	phone = forms.CharField(max_length=20, required=False)
	picture = forms.ImageField()