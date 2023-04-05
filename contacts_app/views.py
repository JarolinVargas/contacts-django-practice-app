from django.shortcuts import get_object_or_404, render, redirect
from .models import Contact

# Create your views here.
def contacts(request):
    myContacts = Contact.objects.all().order_by('-id')
    context = {
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
        return render(request, 'contacts.html')


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
        return render(request, 'contacts.html')





