from django.test import TestCase
from django.urls import reverse
from .models import About
from .forms import ContactForm


class TestAboutView(TestCase):

    def setUp(self):
        """Creates about me content"""
        self.about_content = About(
            title="About Me", content="This is about me.")
        self.about_content.save()

    def test_render_about_page_with_contact_form(self):
        """Verifies get request for about me containing a contact form"""
        response = self.client.get(reverse('about'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'About Me', response.content)
        self.assertIsInstance(
            response.context['contact_form'], ContactForm)
    
    def test_successful_contact_request_submission(self):
        """Test for a user requesting a collaboration"""
        post_data = {
            'name': 'name',
            'email': 'email@email.com',
            'message': 'message'
        }
        response = self.client.post(reverse('about'), post_data)
        self.assertEqual(response.status_code, 200)
        self.assertIn(
            b"Collaboration request sent. I'll respond to you as soon as possible!", response.content)