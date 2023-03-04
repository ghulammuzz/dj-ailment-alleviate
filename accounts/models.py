from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

class BaseUserManager(BaseUserManager):
    def create_user(self, email, username, password, password_2=None, **extra_fields):
        if email is None:
            raise TypeError('Penguna harus memiliki email')
        if password is None:
            raise TypeError('Penguna harus memiliki password')
        # if password != password_2:
        #     raise TypeError('Password tidak cocok')
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
    
    def create_admin(self, username, email, password, password_2, is_admin=True, **extra_fields):
        return self.create_user(email, username, password, password_2, is_admin=is_admin, **extra_fields)
         
class User(AbstractUser):
    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField(unique=True)
    is_peracik = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    
    objects = BaseUserManager()
    
    def _str_(self):
        return self.email
    
class Peracik(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    alamat = models.TextField()
    no_hp = models.CharField(max_length=15)
    class Status(models.TextChoices):
        DITOLAK = 'DITOLAK'
        MENUNGGU = 'MENUNGGU'
        DITERIMA = 'DITERIMA'
    status = models.CharField(max_length=10, choices=Status.choices, default=Status.MENUNGGU)
    sertifikat = models.ImageField(upload_to='sertifikat')
    gambar_pendukung = models.ImageField(upload_to='gambar_pendukung', blank=True, null=True)
    
    def __str__(self):
        return self.user.username
    
class Admin(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    alamat = models.TextField()
    no_hp = models.CharField(max_length=15)
    
    def __str__(self):
        return self.user.username
