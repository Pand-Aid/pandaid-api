from django.urls import reverse
from nose.tools import ok_, eq_
from rest_framework.test import APITestCase
import factory
from .factories import UserFactory


class TestMyTestsTestCase(APITestCase):

    def test_if_this_fails(self):
        test="success"
        ok_(test, "fail")


class TestCORSHeadersTestCase(APITestCase):
    """
    Tests the Django CORS Headers package is working properly 
    and Access-Control-Allow-Origin exists in response headers.
    """

    def setUp(self):
        self.url = reverse('api-token-auth/')
        self.user_data = factory.build(dict, FACTORY_CLASS=UserFactory)

    def test_post_request_has_correct_headers(self):
        response = self.client.post(self.url, self.user_data)
        ok_(response.headers["access-control-allow-origin"], "*")

