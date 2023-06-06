from django.shortcuts import get_object_or_404, render, redirect
from .models import Contact
from django.db.models import Q
from django.contrib.auth import login, logout, authenticate
from .forms import UserSignUpForm, UserSignInForm
from django.contrib import messages

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
    return render(request, 'sign_up.html', context={"sign_up_form":form})


def sign_in(request):
    if request.method == 'POST':
        form = UserSignInForm(request.POST)
        print('TEST')
        print(form.is_valid(), form.errors.as_data(), form.non_field_errors())
        #import pdb;pdb.set_trace()
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('contacts')
            else:
                messages.error(request, 'Invalid username or password')
                return render(request, 'sign_in.html', context={"sign_in_form": form, "sign_in_failed":True})
        else:
            messages.error(request, 'Invalid form input')
            print('errors:', form.errors)
            return redirect('contacts')
    else:
        form = UserSignInForm()
        return render(request, 'sign_in.html', context={"sign_in_form": form})


def sign_out(request):
    logout(request)
    return redirect('contacts')
    






