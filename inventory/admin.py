from django.contrib import admin

from inventory.models import Property
from inventory.forms import PropertyAdminForm

# Register your models here.


class PropertyAdmin(admin.ModelAdmin):
	form = PropertyAdminForm

	list_display = ('street_number', 'street_address', 'suite_number', 'city',)
	list_display_links = ('street_address', )
	lists_per_page = 50
	ordering = ['-city']
	search_fields = ['city']
	prepopulated_fields = {'slug': ('street_number', 'street_address')}

admin.site.register(Property, PropertyAdmin)
