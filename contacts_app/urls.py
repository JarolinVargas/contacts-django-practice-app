from django.urls import path
from . import views

urlpatterns = [
    path('', views.contacts, name='contacts'),
    path('submit_contact/', views.submit_contact, name='submit_contact'),
    path('edit_contact/<int:contact_id>/', views.edit_contact, name='edit_contact'),
    path('search_contacts/', views.search_contacts, name='search_contacts'),
    path('sign_up/', views.sign_up, name='sign_up'),
    path('sign_out/', views.sign_out, name='sign_out')
]