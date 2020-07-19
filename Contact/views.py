from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Contact


def index(request):
    contact_list = Contact.objects.order_by('-created_at')
    context = {
        'contact_list':contact_list
    }
    return render(request, 'contact/index.html', context)

