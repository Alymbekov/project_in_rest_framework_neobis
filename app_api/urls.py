from django.urls import path
from app_api.views import CourseIdView,CourseListView,index
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    path('',index,name='index'),
    # path('category/',CategoryListView.as_view(),name='category'),
    # path('category/<int:category_id>/',CategoryIdView.as_view()),
    path('courses/', CourseListView.as_view(),name="courses"),
    path('courses/<int:course_id>/',CourseIdView.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
