from django.db import models

# Create your models here.

class Country(models.Model):
	"""
		country model 
	"""
	name = models.CharField(max_length=100)

	def __str__(selft):
		return selft.name