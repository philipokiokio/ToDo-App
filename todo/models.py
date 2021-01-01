from django.db import models
from django.utils import timezone
from django.urls import reverse



# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = ("Category")
        verbose_name_plural = ("Categories")
    
    def __str__(self):
        return self.name


class TodoItems(models.Model):
    title = models.CharField(max_length= 100)
    body = models.TextField()
    created = models.DateField(default= timezone.now().strftime('%Y-%m-%d'))
    due_date = models.DateField(default= timezone.now().strftime('%Y-%m-%d'))
    category = models.ForeignKey(Category,on_delete=models.SET_DEFAULT, default='general')
    completed = models.BooleanField(default= False)
    

    class Meta:
        ordering = ['-created']


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('todo')
