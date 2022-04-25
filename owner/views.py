from django.shortcuts import render, redirect
from django.views.generic import View, ListView, DetailView, CreateView, UpdateView, DeleteView
from owner.models import Admin
from owner.forms import OwnerForm
from django.urls import reverse_lazy

# Create your views here.
class LocationList(ListView):
    model = Admin
    context_object_name = "vacc"
    template_name = "view_lactionlist.html"

class Addlocation(CreateView):
    model = Admin
    form_class = OwnerForm
    template_name = "add_locationa.html"
    success_url = reverse_lazy('location')

class LocationDetail(DetailView):
    model = Admin
    context_object_name = "vacc"
    template_name = "location_detail.html"
    pk_url_kwarg = 'id'
    success_url = reverse_lazy("location")

class Locationedit(UpdateView):
    model = Admin
    form_class = OwnerForm
    template_name = "location_edit.html"
    pk_url_kwarg = 'id'
    success_url = reverse_lazy("location")

class LocationDelete(DeleteView):
    model = Admin
    template_name = "delete.html"
    pk_url_kwarg = 'id'
    success_url = reverse_lazy("location")

