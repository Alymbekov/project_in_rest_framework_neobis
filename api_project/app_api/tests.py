from django.urls import reverse
from .models import *
from apps.category.models import Category
import json
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
        # self.assertEqual(json.loads(response.content), {'id': 14, 'name': 'English Zone'})

class Test_Delete_Course_By_Id(APITestCase):


    def test_delete_course_by_id(self):
        """
        Проверяем правильность удаления курсов по id
        """
        response = self.client.delete('/courses/6/')
        print("delete course id",response.status_code,)
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        # self.assertEqual(json.loads(response.content), [])

class Test_Create_Categories(TestCase):


    def setUp(self):
        """
        Проверяем работоспособность создания категории
        """
        Category.objects.create(
                            name = 'Electrica',
                            imgpath = 'https://image.jpg'
                        )
        print(Category)
    def test_one_category(self):
        variable_of_testing = Category.objects.get(imgpath='https://image.jpg')
        print(variable_of_testing.imgpath)
        self.assertEquals(variable_of_testing.imgpath,'https://image.jpg')
        # self.assertContains('Electrica')
        # self.assertContains('https://image.jpg')

class Test_Create_Course(TestCase):


    def setUp(self):
        """
        Создаем тестовый курс для проверки
        """
        category  = Category.objects.create(
                                    name='language course',
                                    imgpath='https://testimage.jpg'
                                )
        Course.objects.create(
                            name = 'Programming Course',
                            logo = 'logo.jpg',
                            description ='we are so master of this course,because we"ve many masters teacher',
                            category = category,
                        )

    def test_create_course(self):
        get_course_testing = Course.objects.get(name='Programming Course')
        self.assertEquals(get_course_testing.name,'Programming Course')
#
# class Test_Create_Branch(TestCase):
#
#
#     def setUp(self):
#         """
#         Проверяем создание модели branch
#         """
#         # course = Course.objects.create(
#         #
#         #                         )
#         Branch.objects.create(
#                         latitude = 32.58,
#                         longitude = 45.99,
#                         address = 'squares Ala Too',
#                         # course = 'language',
#                     )
#         print(Branch)
#
#     def test_branch_model(self):
#         branch_testing = Branch.objects.get(
#                         latitude = 32.58,
#                         longitude = 45.99,
#                         address = 'squares Ala Too',
#                         # course = 'language',
#                     )
#         self.assertEquals(variable_of_testing.latitude,32.58)
#         self.assertEquals(variable_of_testing.longitude,45.99)
class Test_Create_Contacts(TestCase):
    pass

class Test_Post_Request(APITestCase):
    pass
