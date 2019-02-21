from django.test import TestCase
from rest_framework.test import RequestsClient

client = RequestsClient()
response = client.get('http://127.0.0.1:8000/courses/')
assert response.status_code == 200
