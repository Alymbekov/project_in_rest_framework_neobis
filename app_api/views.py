from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import *
from apps.category.models import Category
from .serializers import *
from rest_framework import generics
from django.shortcuts import render

def index(request):
    return render(request,'index.html',{})

class CourseListView(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

#
# class CategoryListView(generics.ListCreateAPIView):
#     queryset = Category.objects.all()
#     serializer_class = CategorySerializer
#
#
# class CategoryIdView(APIView):
#
#     def get(self, request, category_id):
#         category = Category.objects.filter(pk=category_id)
#         category_serializer = CategorySerializer(category, many=True)
#         return Response(category_serializer.data)
#
#
#     def delete(self, request, category_id):
#         Category.objects.filter(pk=category_id).delete()
#         return HttpResponse()


class CourseIdView(APIView):

    def get(self, request, course_id):
        course = Course.objects.filter(pk=course_id)
        course_serializer = CourseSerializer(course, many=True)
        return Response(course_serializer.data)


    def delete(self, request, course_id):
        Course.objects.filter(pk=course_id).delete()
        return HttpResponse()
