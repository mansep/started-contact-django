from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as login_auth, logout as logout_auth
from django.contrib.auth.decorators import login_required
from django.db.utils import IntegrityError
from django.http import HttpResponse

from django.contrib.auth.models import User

from users.models import Profile
from users.forms import ProfileForm

@login_required
def index(request):
	"""Profile view"""
	profile = request.user.profile
	
	return render(
		request=request, 
		template_name = 'users/profile_view.html',
		context={
			'profile': profile,
			'user': request.user
		}
	)


def update_profile(request):
	"""Update profile user"""
	profile = request.user.profile
	if request.method == 'POST':
		form = ProfileForm(request.POST, request.FILES)
		if form.is_valid():
			data = form.cleaned_data

			profile.phone_number = data['phone']
			profile.picture = data['picture']
			profile.save()

			return redirect('update_profile')
	else:
		form = ProfileForm()	

	return render(
		request=request, 
		template_name = 'users/profile_update.html',
		context={
			'profile': profile,
			'user': request.user,
			'form': form
		}
	)

def login(request):
	"""Login View"""
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']

		user = authenticate(request, username=username, password=password)
		if user:
			login_auth(request, user)
			return redirect('/users')
		else:
			return render(request, 'login.html', {'error': 'Invalid username and password'})


	return render(request, 'login.html')

@login_required
def logout(request):
	logout_auth(request)
	return redirect('login')