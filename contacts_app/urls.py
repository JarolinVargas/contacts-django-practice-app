from django.urls import path
from . import views
from .views import submit_contact, edit_contact, search_contacts

urlpatterns = [
    path('', views.contacts, name='contacts'),
    path('submit_contact/', views.submit_contact, name='submit_contact'),
    path('edit_contact/<int:contact_id>/', views.edit_contact, name='edit_contact'),
    path('search_contacts', views.search_contacts, name='search_contacts'),
]