from django.shortcuts import render

# Create your views here.

from django.views.generic import ListView, CreateView, DetailView
from django.core.urlresolvers import reverse

from inventory.models import Property

class ListPropertyView(ListView):
	model = Property
	template_name = 'property_list.html'


class CreatePropertyView(CreateView):

	model = Property 
	template_name = 'edit_property.html'

	def get_success_url(self):
		return reverse('property-list')

class DetailPropertyView(DetailView):
	model = Property
	template_name = 'property_feed.html'