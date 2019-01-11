from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

from django.contrib.auth.models import User

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from app.models import Country
from contacts.models import Contact
from contacts.forms import ContactForm
import pdb

@login_required
def contacts_list(request):
    """Contacts List view"""
    profile = request.user.profile

    page = request.GET.get('page', 1)
    contacts = Contact.objects.all()
    paginator = Paginator(contacts, 50)
    
    try:
        contact_list = paginator.page(page)
    except PageNotAnInteger:
        contact_list = paginator.page(1)
    except EmptyPage:
        contact_list = paginator.page(paginator.num_pages)

    return render(
        request=request, 
        template_name = 'contacts/list.html',
        context={
            'profile': profile,
            'contacts': contact_list,
            'user': request.user
        }
    )

@login_required
def contacts_create(request):
    """Create new contact"""
    profile = request.user.profile
    countries = Country.objects.all()
    if request.method == 'POST':
        form = ContactForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.cleaned_data

            new_contact = Contact()
            
            new_contact.id_document = data['id_document']
            new_contact.name = data['name']
            new_contact.type = data['type']

            new_contact.address = data['address']
            new_contact.state = data['state']
            new_contact.city = data['city']
            new_contact.country = Country.objects.get(pk=data['country'])
            new_contact.phone = data['phone']
            new_contact.fax = data['fax']
            new_contact.mobile = data['mobile']
            new_contact.email = data['email']
            new_contact.website = data['website']

            new_contact.picture = data['picture']
            
            
            new_contact.save()

            return redirect('contacts_create')
    else:
        form = ContactForm()	

    return render(
        request=request, 
        template_name = 'contacts/create.html',
        context={
            'profile': profile,
            'user': request.user,
            'countries': countries,
            'error': form.errors
        }
    )