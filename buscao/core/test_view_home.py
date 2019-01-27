from django.test import TestCase


class test_home(TestCase):
    def setUp(self):
        self.resp = self.client.get('/')

    def test_return_code(self):
        """Test Status code"""
        self.assertEqual(200, self.resp.status_code)

    def test_acess_get(self):
        """Test Template"""
        self.assertTemplateUsed(self.resp, 'core/index.html')

    def test_index_template_contains(self):
        """Test contains in template"""
        self.assertContains(self.resp, 'teste')