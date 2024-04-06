from django.test import TestCase
from regex.services import RegexMatchService
from regex.views import index_view
from django.urls import reverse
from regex.fixtures import get_fixtures


class ServiceTests(TestCase):
    def setUp(self):
        self.fixtures = get_fixtures()
        self.service_class = RegexMatchService()

    def test_check_regex_and_get_response(self):
        for fixture in self.fixtures:
            result = self.service_class.check_regex_and_get_response(
                pattern=fixture['pattern'],
                string=fixture['string'],
            )
            self.assertEqual(result, fixture['response'])


class IndexViewTests(TestCase):
    def setUp(self):
        self.view = index_view
        self.fixtures = get_fixtures()
        self.url = reverse(self.view)

    def test_form_submission(self):
        for fixture in self.fixtures:
            expected_result = fixture.pop('response')

            response = self.client.post(self.url, data=fixture)
            self.assertEqual(response.status_code, 200)

            context_data = response.context

            self.assertIn('response', context_data)
            self.assertEqual(context_data['response'], expected_result)
