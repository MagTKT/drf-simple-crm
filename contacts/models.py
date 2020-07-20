from django.db import models
from django.urls import reverse



class Contact(models.Model):
    first_name = models.CharField(verbose_name='Nom',max_length=50, blank=False)
    last_name = models.CharField(verbose_name='Prénom',max_length=50, blank=False)
    email = models.EmailField(verbose_name='Adresse e-mail', blank=False)
    phone_number = models.IntegerField(verbose_name='Téléphone', null=True, blank=True)
    tag = models.CharField(verbose_name='Catégorie',max_length=50, blank=False)
    created_at = models.DateTimeField(verbose_name='Date de création', auto_now_add=True)

    class Meta:
        ordering = ['created_at']

    def get_absolute_url(self): # new
        return reverse('contact_detail', args=[str(self.id)])