from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(
        max_length=15, 
        blank=True, 
        null=True
    )
    date_joined = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    avatar = models.ImageField(upload_to='avatars/',
                               default='default_avatars/default_avatar.png',
                               null=True,
                               blank=True)
    
     # Solucionar los conflictos de 'groups' y 'user_permissions'
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customuser_set',  # Evitar el conflicto con el modelo auth.User
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups'
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customuser_permissions',  # Evitar el conflicto con el modelo auth.User
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions'
    )
