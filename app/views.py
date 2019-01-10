from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as login_auth, logout as logout_auth
from django.contrib.auth.decorators import login_required
from django.db.utils import IntegrityError
from django.http import HttpResponse

from django.contrib.auth.models import User

from users.models import Profile

@login_required
def dashboard_view(request):
	"""Dashboard view"""
	profile = request.user.profile
	
	return render(
		request=request, 
		template_name = 'app/dashboard.html',
		context={
			'profile': profile,
			'user': request.user
		}
	)