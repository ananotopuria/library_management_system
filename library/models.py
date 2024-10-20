from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    full_name = models.CharField(max_length=100)
    personal_number = models.CharField(max_length=20, unique=True)
    birth_date = models.DateField()
    
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_set', 
        blank=True,
        help_text='The groups this user belongs to.'
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_permissions_set',  
        blank=True,
        help_text='Specific permissions for this user.'
    )

class Author(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name

class Genre(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    genre = models.ManyToManyField(Genre)
    published_date = models.DateField()
    stock = models.PositiveIntegerField()

    def __str__(self):
        return self.title
