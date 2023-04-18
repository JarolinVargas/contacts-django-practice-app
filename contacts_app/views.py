from django.shortcuts import get_object_or_404, render, redirect
from .models import Contact
from django.db.models import Q

homeTemplate = 'index.html'

# Create your views here.
def contacts(request):
    myContacts = Contact.objects.all().order_by('-id')
    context = {
        'my_contacts': myContacts
    }
    return render(request, homeTemplate, context)


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
            if len(filter) == 0:
                return redirect('no_results')
            context = {'my_contacts': filter, 'query': query}
            return render(request, homeTemplate, context)
        else:
            return render(request, homeTemplate)
    return render(request, homeTemplate)







