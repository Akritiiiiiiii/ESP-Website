from django.test import TestCase
from django.urls import reverse

class EditClassViewTest(TestCase):

    def test_editclass_page_loads(self):
        response = self.client.get("/editclass/")
        self.assertIn(response.status_code, [200, 302])


class MakeAClassViewTest(TestCase):

    def test_makeaclass_page_loads(self):
        response = self.client.get("/makeaclass/")
        self.assertIn(response.status_code, [200, 302])
