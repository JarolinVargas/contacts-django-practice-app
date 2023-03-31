from django.shortcuts import render, redirect
from .models import Contact

# Create your views here.
def contacts(request):
    context = {'my_message': 'Hello, Django!'}
    return render(request, 'contacts.html', context)

def submit_contact(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')

        new_contact = Contact(first_name=first_name, last_name=last_name, email=email, phone=phone)
        new_contact.save()

        return redirect('contacts') 
    else:
        return render(request, 'submit_contact.html')

