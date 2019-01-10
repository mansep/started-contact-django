from django.urls import path

from . import views

urlpatterns = [
    path('me/', views.profile_view, name='profile_view'),
    path('password/', views.change_password, name='change_password'),
	path('login/', views.login, name='login'),
	path('logout/',views.logout, name='logout'),

	path('profile', views.profile_update, name='profile_update') 
]