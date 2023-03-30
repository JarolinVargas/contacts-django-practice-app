from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

def contacts(request):
    context = {'my_message': 'Hello, Django!'}
    return render(request, 'contacts.html', context)