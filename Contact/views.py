from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

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

class ContactUpdate(UpdateView): 
    model = Contact

class ContactDelete(DeleteView): 
    model = Contact