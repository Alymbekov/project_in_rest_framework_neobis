from django.urls import reverse
from .models import *
from django.test import TestCase
from rest_framework import status
from rest_framework.test import  APITestCase
import unittest
# loader = unittest.TestLoader()
# start_dir = 'project_in_rest_framework_neobis/api_project/apps/app_api/tests.py'
# suite = loader.discover(start_dir)
#
# runner = unittest.TextTestRunner()
# runner.run(suite)

class Test_Get_Course(APITestCase):
    def test_get_course(self):
        """
        Проверяем get запрос на корректность
        """
        print('asasdasd')
        url = reverse('courses')
        response = self.client.get(url)

        self.assertEqual(response.status_code,status.HTTP_200_OK)
