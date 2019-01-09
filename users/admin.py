from django.contrib import admin

# Register your models here.

from users.models import Profile
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):

	list_display = ('pk', 'user', 'phone', 'picture')
	list_display_links = ('pk', 'user')
	list_editable = ('phone', 'picture')
	search_fields = ('use__email', 'user__username', 'user__first_name', 'user__last_name', 'phone')
	list_filter = ('created', 'modified', 'user__is_active', 'user__is_staff')

	fieldsets = (
		('Profile', {
			'fields': (('user', 'picture')),
		}),
		('Extra info', {
			'fields': (
					('phone'),
			),
		}),
		('Metadata', {
			'fields': (('created', 'modified'),),
		})
	)	

	readonly_fields = ('created', 'modified')