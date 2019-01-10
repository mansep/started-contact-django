from django.urls import path

from . import views

urlpatterns = [
    path('me/', views.index, name='index'),
    path('password/', views.change_password, name='change_password'),
	path('login/', views.login, name='login'),
	path('logout/',views.logout, name='logout'),

	path('profile', views.update_profile, name='update_profile') 
]