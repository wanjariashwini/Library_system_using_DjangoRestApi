from django.db import models


# Create your models here.

class Book_status(models.Model):
    book_id = models.IntegerField
    issued_to_name = models.CharField(max_length=255)
    issued_date = models.DateField(auto_now_add=True)
    due_date = models.DateField
    return_date = models.DateField(default=None)
    fine = models.IntegerField(default=None)


class Student_Book_status(models.Model):
    book_id = models.IntegerField
    issued_date = models.DateField(auto_now_add=True)
    due_date = models.DateField
    return_date = models.DateField(default=None)
    fine = models.IntegerField(default=None)


class Student(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, primary_key=True)
    password = models.CharField(max_length=255)


class Admin(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, primary_key=True)
    password = models.CharField(max_length=255)
