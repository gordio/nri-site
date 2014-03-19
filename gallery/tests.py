from django.test import TestCase
from django.test.client import Client
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User


class GalleryTestCase(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User(username='fakeuser', is_staff=False)
        self.user.set_password('pass')
        self.user.save()
        self.staff = User(username='fakestaff', is_staff=True)
        self.staff.set_password('pass')
        self.staff.save()
        self.admin = User(username='fakeadmin', is_superuser=True)
        self.admin.set_password('pass')
        self.admin.save()

    def test_empty_page_rendering(self):
        response = self.client.get(reverse('gallery'))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No photos")

    def test_admin_panel_link(self):
        # Hide for User
        self.client.login(username=self.user.username, password="pass")

        response = self.client.get(reverse('gallery'))
        self.assertEqual(response.context["user"], self.user)
        self.assertEqual(response.status_code, 200)
        self.assertNotContains(response, "Admin Panel")

        self.client.logout()

        # Hide for anonymous
        response = self.client.get(reverse('gallery'))
        self.assertEqual(response.status_code, 200)
        self.assertNotContains(response, "Admin Panel")

        # Show for Stuff
        self.client.login(username=self.staff.username, password="pass")

        response = self.client.get(reverse('gallery'))
        self.assertEqual(response.context["user"], self.staff)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Admin Panel")

        self.client.logout()

        # Show for Admin
        self.client.login(username=self.admin.username, password="pass")

        response = self.client.get(reverse('gallery'))
        self.assertEqual(response.context["user"], self.admin)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Admin Panel")

        self.client.logout()
