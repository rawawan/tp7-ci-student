from django.db import models

class University(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.name
 
class Student(models.Model): 
    first_name = models.CharField(max_length=100) 
    last_name = models.CharField(max_length=100) 
    email = models.EmailField(unique=True)
    university = models.ForeignKey(University, on_delete=models.CASCADE, related_name='students')
 
    def __str__(self): 
        return f"{self.first_name} {self.last_name}"