from django.contrib import admin

# Register your models here.

from contacts.models import Contact
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):

	list_display = ('pk', 'name', 'phone', 'email')
	

	fieldsets = (
		('ID', {
			'fields': (('id_document', 'name')),
		}),
		('Address', {
			'fields': (
					(('address', 'state', 'city', 'country')),
			),
		}),
		('Contact', {
			'fields': (
					(('email','phone','fax','mobile','website')),
			),
		}),
		('Picture', {
			'fields': (
					('picture'),
			),
		}),
		('Metadata', {
			'fields': (('created', 'modified'),),
		})
	)

	readonly_fields = ('created', 'modified')
"""
    
            new_contact.state = data['state']
            new_contact.city = data['city']
            new_contact.country = Country.objects.get(pk=data['country'])
            new_contact.phone = data['phone']
            new_contact.fax = data['fax']
            new_contact.mobile = data['mobile']
            new_contact.email = data['email']
            new_contact.website = data['website']

            new_contact.picture = data['picture']"""