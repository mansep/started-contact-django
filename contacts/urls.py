from django.urls import path

from . import views

urlpatterns = [
    path('', views.contacts_list, name='contacts_list'),
    path('create/', views.contacts_create, name='contacts_create')
]