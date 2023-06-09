from django.shortcuts import get_object_or_404, render, redirect
from .models import Contact
from django.db.models import Q
from django.contrib.auth import login, logout, authenticate
from .forms import UserSignUpForm, UserSignInForm
from django.contrib import messages

homeTemplate = 'base.html'

# Create your views here.
def contacts(request):
    user = request.user
    myContacts = None
    if user.is_authenticated:
        myContacts = Contact.objects.filter(user=user).order_by('-id')
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

        new_contact = Contact(user=request.user, full_name=full_name, email=email, phone=phone)
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
        user = request.user
        query = request.POST.get('query')
        if query:
            filter = Contact.objects.filter(
                Q(user=user) & (Q(full_name__icontains=query) | Q(email__icontains=query) | Q(phone__icontains=query))
            )
            context = {
                'username': user.username,
                'my_contacts': filter,
                'query': query
            }
            return render(request, 'contacts.html', context)
        else:
            context = {
                'username': user.username,
                'my_contacts': None,
                'query': None
            }
            return render(request, 'contacts.html', context)
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
            return redirect('contacts')
    else:
        form = UserSignInForm()
        return render(request, 'sign_in.html', context={"sign_in_form": form})


def sign_out(request):
    logout(request)
    return redirect('contacts')


def delete_account(request):
    if request.method == 'POST':
        form = UserSignInForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user == request.user:
                logout(request)
                user.delete()
                return render(request, 'contacts.html', context={"account_deleted": True})
            else:
                messages.error(request, 'Invalid username or password')
                return render(request, 'sign_in.html', context={"sign_in_form": form, "sign_in_failed":True, "delete_account": True})

        return render(request, 'sign_in.html', context={"sign_in_form": form, "delete_account": True})
    else:
        form = UserSignInForm()
        return render(request, 'sign_in.html', context={"sign_in_form": form, "delete_account": True})

    






