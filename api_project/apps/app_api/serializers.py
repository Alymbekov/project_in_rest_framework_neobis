from rest_framework import serializers
from .models import *



class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = (
            'id',
            'name'
            )


class BranchSerializer(serializers.ModelSerializer):

    class Meta:
        model = Branch
        fields = (
            'id',
            'course',
            'latitude',
            'longitude',
            'address'
        )
        read_only_fields = ('course',)


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = (
            'id',
            'course',
            'value',
            'type'
        )
        read_only_fields = ('course',)

class CourseSerializer(serializers.ModelSerializer):
    branches = BranchSerializer(many=True)
    contacts = ContactSerializer(many=True)

    class Meta:
        model = Course
        fields = [
            'id',
            'name',
            'description',
            'category',
            'logo',
            'contacts',
            'branches',
        ]

    def created(func):
        def wrapper():
            result = func()
            return result
        return wrapper


    def create(self,validated_data):
        contacts = validated_data.pop('contacts')
        branches = validated_data.pop('branches')
        course = Course.objects.create(**validated_data)
        for contact in contacts:
            Contact.objects.create(**contact,course=course)

        for branch in branches:
            Branch.objects.create(**branch,course=course)

        return course

    # def create_branch(self, validated_data):
    #     branches = validated_data.pop('branches')
    #     course = Course.objects.create(**validated_data)
    #
    #     return course
