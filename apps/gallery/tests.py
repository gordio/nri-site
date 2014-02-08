from django.test import TestCase
from django.test.client import Client
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User


class GalleryTestCase(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create(username='fakeuser',
            password="fakepass", is_staff=False)
        self.staff = User.objects.create(username='fakestaff',
            password="fakepass", is_staff=True)    
        self.admin = User.objects.create(username='fakeadmin',
            password="fakepass", is_superuser=True)

    def test_empty_page_rendering(self):
        response = self.client.get(reverse('gallery'))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No photos")
        # TestCase.assertTemplateUsed(response, 'gallery/photo_list.html')

    def test_admin_panel_link(self):
        # FIXME: How test_client_get as user?
        # no Link for User
        self.client.login(username=self.user.username,
            password=self.user.password)

        response = self.client.get(reverse('gallery'))
        print("\n", response.context["user"], "\n")
        self.assertEqual(response.status_code, 200)
        self.assertNotContains(response, "Admin Panel")

        self.client.logout()

        # Link for Stuff
        self.client.login(username=self.staff.username,
            password=self.staff.password)

        response = self.client.get(reverse('gallery'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Admin Panel")

        self.client.logout()

        # Link for Admin
        self.client.login(username=self.admin.username,
            password=self.admin.password)

        response = self.client.get(reverse('gallery'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Admin Panel")

        self.client.logout()
