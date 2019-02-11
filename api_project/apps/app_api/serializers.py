from rest_framework import serializers
from .models import *



class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ('id','name')


class BranchSerializer(serializers.ModelSerializer):

    class Meta:
        model = Branch
        fields = ('id', 'course','latitude','longitude','address')



class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ('id', 'course','value')


class CourseSerializer(serializers.ModelSerializer):
    branches = BranchSerializer(many=True)
    contacts = ContactSerializer(many=True)

    class Meta:
        model = Course
        fields = ('id', 'name', 'description', 'category', 'logo', 'contacts', 'branches')


    def create(self, validated_data,*args):
        branches_data = validated_data.pop('branches')
        contacts_data = validated_data.pop('contacts')
        course = Course.objects.create(**validated_data)
        for contact in contacts_data:
            Contact.objects.create(*args , **contact)
        for branch in branches_data:
            Branch.objects.create( *args, **branch)

        return course
# class CourseSerializer(serializers.ModelSerializer):
#     branches = BranchSerializer(many=True)
#     contacts = ContactSerializer(many=True)
#
#     class Meta:
#         model = Course
#         fields = ('id', 'name', 'description', 'category', 'logo', 'contacts', 'branches')
#
#
#     def create(self, validated_data):
#         course = Course.objects.create(**validated_data)
#         return course
