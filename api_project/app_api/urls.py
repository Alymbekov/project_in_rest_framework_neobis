from django.urls import path
from app_api.views import CourseIdView,CourseListView
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    path('courses/', CourseListView.as_view(),name="courses"),
    path('courses/<int:course_id>/',CourseIdView.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)