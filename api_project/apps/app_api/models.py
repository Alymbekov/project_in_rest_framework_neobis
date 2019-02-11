from django.db import models

from apps.category.models import Category

class Course(models.Model):
    name = models.CharField(max_length=155)
    description = models.TextField()
    category = models.ForeignKey(Category,related_name='courses',on_delete=models.CASCADE)
    logo =models.CharField(max_length=155)

    def __str__(self):
        return self.name

class Branch(models.Model):
    latitude =  models.FloatField()
    longitude = models.FloatField()
    address = models.CharField(max_length=255);
    course = models.ForeignKey(Course,related_name='branches',on_delete=models.CASCADE)

class Contact(models.Model):
    course = models.ForeignKey(Course,related_name='contacts',on_delete=models.CASCADE)
    CONTACT_CHOISES = (
        (1, "PHONE"),
        (2, "FACEBOOK"),
        (3, "EMAIL"),

    )
    type = models.PositiveIntegerField(choices=CONTACT_CHOISES,default=3)
    value = models.CharField(max_length=155)

    def __str__(self):
        return self.value
