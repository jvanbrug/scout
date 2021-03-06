from django.core.urlresolvers import resolve
from django.http import HttpRequest
from django.template.loader import render_to_string
from django.test import TestCase

from layout.views import home


class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page(self):
        found = resolve('/')
        self.assertEqual(found.func, home)

    def test_home_page_returns_correct_html(self):
        expected_html = render_to_string('home.html')
        request = HttpRequest()
        response = home(request)
        actual_html = response.content.decode()
        self.assertEqual(actual_html, expected_html)

    def test_home_page_can_save_a_POST_request(self):
        query = 'python yield'
        expected_html = render_to_string(
            'home.html',
            {'query': query}
        )
        request = HttpRequest()
        request.method = 'POST'
        request.POST['query'] = query
        response = home(request)
        actual_html = response.content.decode()
        self.assertIn(query, actual_html)
        self.assertEqual(actual_html, expected_html)
