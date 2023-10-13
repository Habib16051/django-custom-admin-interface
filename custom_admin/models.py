from django.db import models

# Create your models here.
class Person(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    contact = models.IntegerField()
    date = models.DateField(auto_now_add=True)
    
    class Meta:
        ordering = ['-date']
        
    def __str__(self):
        return self.first_name
    
    class Meta:
        verbose_name_plural = 'Person'
    

class Course(models.Model):
    name = models.CharField(max_length=250)
    author = models.CharField(max_length=200)
    
