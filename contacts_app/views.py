from django.shortcuts import get_object_or_404, render, redirect
from .models import Contact
from django.db.models import Q
from django.contrib.auth import login, logout
from .forms import UserSignUpForm

homeTemplate = 'base.html'

# Create your views here.
def contacts(request):
    myContacts = Contact.objects.all().order_by('-id')
    user = request.user
    context = {
        'username': user.username,
        'my_contacts': myContacts
    }
    return render(request, 'contacts.html', context)


def submit_contact(request):
    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')

        new_contact = Contact(full_name=full_name, email=email, phone=phone)
        new_contact.save()

        return redirect('contacts') 
    else:
        return render(request, homeTemplate)


def edit_contact(request, contact_id):
    contact = get_object_or_404(Contact, id=contact_id)

    if request.method == 'POST':
        contact.full_name = request.POST.get('full_name')
        contact.email = request.POST.get('email')
        contact.phone = request.POST.get('phone')

        delete = request.POST.get('delete')

        if delete == 'on':
            contact.delete()
        else:
            contact.save()

        return redirect('contacts')
    else:
        return render(request, homeTemplate)


def search_contacts(request):
    if request.method == 'POST':
        query = request.POST.get('query')
        if query:
            filter = Contact.objects.filter(
                Q(full_name__icontains=query) | Q(email__icontains=query) | Q(phone__icontains=query)
            )
            context = {'my_contacts': filter, 'query': query}
            return render(request, 'contacts.html', context)
        else:
            return render(request, 'contacts.html')
    return render(request, homeTemplate)


def sign_up(request):
    if request.method == 'POST':
        form = UserSignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('contacts')
    else:
        form = UserSignUpForm()
    return render(request, 'sign_up.html', context={"register_form":form})


def sign_out(request):
    logout(request)
    return redirect('sign_up')
    






