from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.urls import reverse

from django.views.generic import ListView, DetailView 
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Contact
from .forms import ContactForm


class ContactList(ListView): 
    model = Contact

class ContactDetail(DetailView): 
    model = Contact

class ContactCreate(CreateView): 
    model = Contact
    form_class = ContactForm

class ContactUpdate(UpdateView): 
    model = Contact
    form_class = ContactForm


class ContactDelete(DeleteView): 
    model = Contact
    
    def get_success_url(self):
            return reverse('contact_list')