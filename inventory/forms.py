from django import forms
from inventory.models import Property

class PropertyAdminForm(forms.ModelForm):
	class Meta:
		model = Property
