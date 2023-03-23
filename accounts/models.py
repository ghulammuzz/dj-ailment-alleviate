from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

class BaseUserManager(BaseUserManager):
    def create_user(self, email, username, password, password_2, **extra_fields):
        if email is None:
            raise TypeError('Penguna harus memiliki email')
        if password is None:
            raise TypeError('Penguna harus memiliki password')
        user = self.model(username=username, email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save()
        return user 
    
    def create_superuser(self, username, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        user = self.create_user(email, username, password, **extra_fields)    
        return user
    
    
    def create_peracik(self, email, username, password, password_2, is_peracik=True, **extra_fields):
        return self.create_user(email, username, password, password_2, is_peracik=is_peracik, **extra_fields)
         
class User(AbstractUser):
    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField(unique=True)
    is_peracik = models.BooleanField(default=False)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    
    objects = BaseUserManager()
    
    def _str_(self):
        return self.email
    
class Peracik(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    address = models.TextField()
    phone_number = models.CharField(max_length=15)
    class Status(models.TextChoices):
        CANCELED = 'CANCELED'
        WAITING = 'WAITING'
        ACCEPTED = 'ACCEPTED'
    status = models.CharField(max_length=10, choices=Status.choices, default=Status.WAITING)
    class Type(models.TextChoices):
        INSTITUSI = 'INSTITUSI'
        TRADITIONAL = 'TRADITIONAL'
    type = models.CharField(max_length=15, choices=Type.choices, default=Type.TRADITIONAL)
    message_status = models.TextField(blank=True, null=True)
    certificate = models.ImageField(upload_to='certificate', blank=True, null=True)
    supporting_image = models.ImageField(upload_to='supporting_image', blank=True, null=True)
    
    def __str__(self):
        return self.user.username