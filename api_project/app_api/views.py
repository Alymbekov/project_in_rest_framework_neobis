from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializers import *
from rest_framework import generics
from django.shortcuts import render

def index(request):
    return render(request,'index.html',{})

class CourseListView(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class CourseIdView(APIView):

    def get(self, request, course_id):
        course = Course.objects.filter(pk=course_id)
        course_serializer = CourseSerializer(course, many=True)
        return Response(course_serializer.data)


    def delete(self, request, course_id):
        Course.objects.filter(pk=course_id).delete()
        return HttpResponse()
