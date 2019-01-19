from django.shortcuts import redirect
from django.urls import reverse

class ProfileMiddleware:

	def __init__(self, get_response):
		self.get_response = get_response


	def __call__(self, request):
		
		if request.path not in [reverse('profile_update'), reverse('logout'), reverse('login')]:
			try:
				profile = request.user.profile
			except Exception as e:
				return redirect('profile_update')
			
			if not profile:
				return redirect('profile_update')
				
		response = self.get_response(request)
		return response