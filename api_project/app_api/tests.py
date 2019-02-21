from django.urls import reverse
from .models import *
from django.test import TestCase
from rest_framework import status
from rest_framework.test import  APITestCase,RequestsClient
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

class Test_Get_Course_By_Id(APITestCase):


    def test_get_course_by_id(self):
        """
        Проверяем get запрос по id на корректность
        """
        client = RequestsClient()
        # response = client.get('http://127.0.0.1:8000/courses/14')
        response = self.client.get('/courses/14/')
        print(response)
        # assert response.status_code == HTTP_200_OK
        self.assertEqual(response.status_code,status.HTTP_200_OK)
