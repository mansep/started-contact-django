from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as login_auth, logout as logout_auth
from django.contrib.auth.decorators import login_required
from django.db.utils import IntegrityError
from django.http import HttpResponse

from django.contrib.auth.models import User

from users.models import Profile
from users.forms import ProfileForm, ChangePasswordForm

@login_required
def profile_view(request):
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

@login_required
def profile_update(request):
	"""Update profile user"""
	profile = request.user.profile
	if request.method == 'POST':
		form = ProfileForm(request.POST, request.FILES)
		if form.is_valid():
			data = form.cleaned_data

			user = request.user

			user.first_name = data['first_name']
			user.last_name = data['last_name']
			user.save()

			profile.phone = data['phone']
			profile.picture = data['picture']
			profile.save()

			return redirect('profile_update')
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

@login_required
def change_password(request):
	"""Change password user"""
	if request.method == 'POST':
		form = ChangePasswordForm(request.POST)
		if form.is_valid():
			data = form.cleaned_data
			if data['new_password'] == data['retry_password']:
				user = authenticate(request, username=request.user.username, password=data['current_password'])
				if user:
					user.set_password(data['new_password'])
					user.save()
					return redirect('profile_view')
				else:
					return render(request, 'users/change_password.html', {'error': 'Invalid username and password'})
			else:
				return render(request, 'users/change_password.html', {'error': 'New password does not match'})
	else:
		form = ChangePasswordForm()	

	return render(
		request=request, 
		template_name = 'users/change_password.html',
		context={
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
			return redirect('profile_view')
		else:
			return render(request, 'login.html', {'error': 'Invalid username and password'})


	return render(request, 'login.html')

@login_required
def logout(request):
	logout_auth(request)
	return redirect('login')