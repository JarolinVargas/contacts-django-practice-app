from django.urls import path
from . import views
from .views import submit_contact, edit_contact

urlpatterns = [
    path('', views.contacts, name='contacts'),
    path('submit_contact/', submit_contact, name='submit_contact'),
    path('edit_contact/<int:contact_id>/', edit_contact, name='edit_contact')
]