from django.urls import path

from . import views

urlpatterns = [
    path('', views.contacts_list, name='contacts_list'),
    path('create/', views.contacts_create, name='contacts_create'),
    path('edit/<int:id>/', views.contacts_edit, name='contacts_edit'),
    path('view/<int:id>/', views.contacts_view, name='contacts_view'),
]