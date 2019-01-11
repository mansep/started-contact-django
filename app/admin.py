from django.contrib import admin

from app.models import Country

@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):

	list_display = ('pk', 'name',)
	fieldsets = (
		('Country', {
			'fields': ('name',),
		}),
	)