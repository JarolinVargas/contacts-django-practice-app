from django.urls import path
from . import views
from .views import submit_contact

urlpatterns = [
    path('', views.contacts, name='contacts'),
    path('submit_contact/', submit_contact, name='submit_contact'),
]