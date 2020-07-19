from django.db import models


class Contact(models.Model):
    first_name = models.CharField(verbose_name='Nom',max_length=50)
    last_name = models.CharField(verbose_name='Prénom',max_length=50)
    email = models.EmailField(verbose_name='Adresse e-mail', blank=True)
    phone_number = models.IntegerField(verbose_name='Téléphone')
    tag = models.CharField(verbose_name='Catégorie',max_length=50)
    created_at = models.DateTimeField(verbose_name='Date de création', auto_now_add=True)

    class Meta:
        ordering = ['created_at']