from django.db import models
from django.contrib.auth.models import User
# Create your models here.


from django.db import models
from django.contrib.auth.models import User


# Category Model
class Category(models.Model):

  

    name = models.CharField(max_length=100)

    description = models.TextField(blank=True, null=True)

    color = models.CharField(max_length=20, default="#1769aa")

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name



class Task(models.Model):

    PRIORITY_CHOICES = [
        ('Low', 'Low'),
        ('Medium', 'Medium'),
        ('High', 'High'),
    ]

    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('In Progress', 'In Progress'),
        ('Completed', 'Completed'),
    ]

  

    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='tasks'
    )

    title = models.CharField(max_length=200)

    description = models.TextField(blank=True, null=True)

    priority = models.CharField(
        max_length=10,
        choices=PRIORITY_CHOICES,
        default='Medium'
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='Pending'
    )

    due_date = models.DateField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    
    
    
    
