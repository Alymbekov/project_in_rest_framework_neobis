from .models import *
from django.test import TestCase
from rest_framework import status
from rest_framework.test import  APITestCase

class Test_Get_Course(APITestCase):
    def test_get_course(self):
        """
        Проверяем get запрос на корректность
        """
        url = reverse('courses')
        response = self.client.get(url)

        self.assertEqual(response.status_code,status.HTTP_200_OK)
