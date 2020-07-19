from django.test import TestCase

from .models import Contact
from django.urls import reverse

    
class DetailPageTestCase(TestCase):
    
    # test en base de données
    def test_detail_page_returns_200(self):
        name = Contact.objects.create(first_name="Transmission Impossible")
        name_id = Contact.objects.get(first_name='Transmission Impossible').id
        response = self.client.get(reverse('contact_detail', args=(name_id,)))
        self.assertEqual(response.status_code, 200)

    # test that detail page returns a 404 if the item does not exist
    def test_detail_page_returns_404(self):
        name = Contact.objects.create(first_name="Transmission Impossible")
        name_id = Contact.objects.get(first_name='Transmission Impossible').id + 1
        response = self.client.get(reverse('contact_detail', args=(name_id,)))
        self.assertEqual(response.status_code, 404)

class CreateContactTestCase(TestCase):
    
    def setUp(self):
        Contact.objects.create(
            first_name="test", 
            last_name='titi', 
            email="test@gmail.forever", 
            phone_number=0000000000, 
            tag='dev'
        )
        self.contact = Contact.objects.get(
            first_name="test", 
            last_name='titi', 
            email="test@gmail.forever", phone_number=0000000000, 
            tag='dev'
        )

    # teste l'affichage des contacts
    def test_index(self):
        """
        Affichage de la page d'accueil : liste des contacts.
        """
        response = self.client.get(reverse('contact_list'))
        self.assertEqual(response.status_code, 200)

    # tester la creation d'un bon contact
    def test_new_contact_is_registered(self):
        contact_id = self.contact.id
        first_name = self.contact.first_name
        last_name = self.contact.last_name
        phone_numer = self.contact.phone_number
        email = self.contact.email
        tag = self.contact.tag
        response = self.client.post(reverse('contact_create', args=(contact_id,)), {
            'first_name': first_name,
            'last_name': last_name,
            'email': email,
            'phone_number': 0000000000,
            'email': email,
            'tag': tag
        })
        new_contacts = Contact.objects.count()
        self.assertEqual(new_contacts, old_contacts + 1)

    # tester la creation d'un mauvais contact
    def test_new_contact_is_not_registered(self):
        contact_id = self.contact.id
        first_name = self.contact.first_name
        last_name = self.contact.last_name
        phone_numer = self.contact.phone_number
        email = self.contact.email
        tag = self.contact.tag
        response = self.client.post(reverse('contact_create', args=(contact_id,)), {
            'first_name': first_name,
            'last_name': last_name,
            'email': 'tutu',
            'phone_number': 0000000000,
            'email': email,
            'tag': tag
        })
        self.assertEqual(new_contacts, old_contacts + 1)


    # tester la modification d'un bon contact
    def test_modification_contact(self):
        contact_id = self.contact.id
        first_name = self.contact.first_name
        last_name = self.contact.last_name
        phone_numer = self.contact.phone_number
        email = self.contact.email
        tag = self.contact.tag
        response = self.client.post(reverse('contact_update', args=(contact_id,)), {
            'first_name': first_name,
            'last_name': last_name,
            'phone_number': 0000000000,
            'email': email,
            'tag': tag
        })
        new_contacts = Contact.objects.count()
        self.assertEqual(response.status_code, 200)
    # tester la modification d'un mauvais contact

    # tester la suppression d'un contact

