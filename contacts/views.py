from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

from django.contrib.auth.models import User

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from app.models import Country
from contacts.models import Contact
from contacts.forms import ContactForm
from started_admin import utils

@login_required
def contacts_list(request):
    """Contacts List view"""
    profile = request.user.profile

    page = request.GET.get('page', 1)
    contacts = Contact.objects.all()
    paginator = Paginator(contacts, 25)
    
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


@login_required
def contacts_update(request, id):
    """Contacts Edit view"""
    profile = request.user.profile
    countries = Country.objects.all()
    error = False   
    success = False

    try:
        contact = Contact.objects.get(pk=id)
        if request.method == 'POST':
            form = ContactForm(request.POST, request.FILES)
            if form.is_valid():
                data = form.cleaned_data
                
                contact.id_document = data['id_document']
                contact.name = data['name']
                contact.type = data['type']

                contact.address = data['address']
                contact.state = data['state']
                contact.city = data['city']
                contact.country = Country.objects.get(pk=data['country'])
                contact.phone = data['phone']
                contact.fax = data['fax']
                contact.mobile = data['mobile']
                contact.email = data['email']
                contact.website = data['website']
                if data['picture']:
                    contact.picture = data['picture']
                
                contact.save()
                success = "Successfully edited contact"
        else:
            form = ContactForm()	
    except Contact.DoesNotExist as e:
        contact = Contact()
        error = "Contact not exist"
    except Exception as e:
        contact = Contact()
        error = e


    return render(
        request=request, 
        template_name = 'contacts/update.html',
        context={
            'profile': profile,
            'contact': contact,
            'countries': countries,
            'user': request.user,
            'error': error,
            'success': success
        }
    )


@login_required
def contacts_view(request, id):
    """Contacts view"""
    profile = request.user.profile
    contact = Contact.objects.get(pk=id)    

    return render(
        request=request, 
        template_name = 'contacts/view.html',
        context={
            'profile': profile,
            'contact': contact,
            'user': request.user
        }
    )


@login_required
def contacts_delete(request, id):
    """Contacts delete"""
    profile = request.user.profile
    success = False
    error = False
    try:
        contact = Contact.objects.get(pk=id)
    except Contact.DoesNotExist as e:
        contact = Contact()
        error = "Contact not exist"
    except Exception as e:
        contact = Contact()
        error = e

    if request.method == 'POST':
        contact.delete()
        success = "Contact removed successfully"
    return render(
        request=request, 
        template_name = 'contacts/delete.html',
        context={
            'profile': profile,
            'contact': contact,
            'user': request.user,
            'success': success,
            'error': error
        }
    )


@login_required
def contacts_to_pdf(request, id):
    """Export to PDF"""

    contact = Contact.objects.get(pk=id)
    host = request.build_absolute_uri('/')[:-1] #Image url
    
    context = {'contact': contact, 'host': host}
    return utils.html_to_pdf(request, 'pdf/contact.html',  context, contact.id_document)

    
@login_required
def contacts_to_xls(request):
    """Export to xls"""

    contact = Contact.objects.all()
    columns = ['ID', 'Name', "Address", "State", "City", "Country", "Phone", "Fax", "Mobile", "Email", "Website", ]
    row = contact.values_list("id_document", "name", "address", "state", "city", "country", "phone", "fax", "mobile", "email", "website", )

    return utils.model_to_xls(request, columns, row, 'contacts')
    
    