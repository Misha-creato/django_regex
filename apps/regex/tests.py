import os
import json

from django.test import TestCase
from django.urls import reverse

from regex.services import check_regex_and_get_response


CUR_DIR = os.path.dirname(__file__)


class ServiceTests(TestCase):
    @classmethod
    def setUp(cls):
        with open(f'{CUR_DIR}/fixtures.json') as file:
            cls.fixtures = json.load(file)

    def test_check_regex_and_get_response(self):
        for fixture in self.fixtures:
            result = check_regex_and_get_response(
                pattern=fixture['pattern'],
                string=fixture['string'],
            )
            self.assertEqual(result, fixture['response'])


class IndexViewTests(TestCase):
    @classmethod
    def setUp(cls):
        with open(f'{CUR_DIR}/fixtures.json') as file:
            cls.fixtures = json.load(file)
        cls.url = reverse('index')

    def test_form_submission(self):
        for fixture in self.fixtures:
            expected_result = fixture.pop('response')

            response = self.client.post(self.url, data=fixture)
            self.assertEqual(response.status_code, 200)

            context_data = response.context

            self.assertIn('response', context_data)
            self.assertEqual(context_data['response'], expected_result)
