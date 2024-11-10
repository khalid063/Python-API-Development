from django.db import models # type: ignore
from django.contrib.auth.models import AbstractUser # type: ignore ## Registration of New User with Password "Model"


# Create your models here.
class User(models.Model):
    age = models.IntegerField()
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name  # Indent this line properly



# Registration of New User with Password "Model"
class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=15, unique=True)
    name = models.CharField(max_length=255)

    # Define custom related_name for groups and user_permissions
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customuser_set',
        blank=True,
        help_text='The groups this user belongs to.',
        related_query_name='customuser',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customuser_set',
        blank=True,
        help_text='Specific permissions for this user.',
        related_query_name='customuser',
    )

    def __str__(self):
        return self.username  # Return the username for string representation