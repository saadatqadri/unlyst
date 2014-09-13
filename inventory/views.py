from django.shortcuts import render

# Create your views here.

from django.views.generic import ListView, CreateView, UpdateView, DetailView
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

	def get_context_data(self, **kwargs):

		context = super(CreatePropertyView, self).get_context_data(**kwargs)
		context['action'] = reverse('property-new')

		return context


class UpdatePropertyView(UpdateView):

	model = Property
	template_name = 'edit_property.html'

	def get_success_url(self):
		return reverse('property-list')

	def get_context_data(self, **kwargs):

		context = super(UpdatePropertyView, self).get_context_data(**kwargs)
		context['action'] = reverse('property-edit', 
			kwargs={'pk': self.get_object().id})

		return context



class DetailPropertyView(DetailView):
	model = Property
	template_name = 'property_detail.html'