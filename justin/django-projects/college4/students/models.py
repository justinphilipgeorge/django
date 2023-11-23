from django.db import models

# Create your models here.

class Department(models.Model):
    name=models.CharField(max_length=255)

    
class Teacher(models.Model):
    name=models.CharField(max_length=255)
    department=models.ForeignKey(Department,on_delete=models.CASCADE)

class Batch(models.Model):
    batch=models.CharField(max_length=255)

class Student(models.Model):
    name=models.CharField(max_length=255)
    batch=models.ForeignKey(Batch,on_delete=models.CASCADE)
    teacher=models.ForeignKey(Teacher,on_delete=models.CASCADE)

