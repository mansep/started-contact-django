from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Profile(models.Model):
	"""
	profile model 
	"""

	user = models.OneToOneField(User, on_delete=models.CASCADE)	
	phone = models.CharField(max_length=20, blank=True)
	picture = models.ImageField(
		upload_to='users/pictures',
		blank=True,
		null=True
	)

	created = models.DateTimeField(auto_now_add=True)
	modified = models.DateTimeField(auto_now=True)

	def __str__(selft):
		return selft.user.username