from django.test import TestCase

from .models import Contact


class ContactModelTests(TestCase):

    def test_verification_of_email_validate(self):
        """
            Verification of email validate
        """
        email = 'email@email.com'
        self.assertEqual(data['email'], 'email@email.com')