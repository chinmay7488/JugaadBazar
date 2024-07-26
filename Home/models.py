from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager

# ----------Custom User Model------------
class UserManager(BaseUserManager):
    def create_user(self, phone_number, password=None, **extra_fields):
        if not phone_number:
            raise ValueError("Phone number is required")

        extra_fields['email'] = self.normalize_email(extra_fields['email'])
        user = self.model(phone_number = phone_number, **extra_fields)
        user.set_password(password)
        user.save(using= self.db)

        return user

    def create_superuser(self, phone_number, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        return self.create_user(phone_number, password, **extra_fields)

class CustomUserModel(AbstractUser):

    username = None
    full_name = models.CharField(max_length=200, default="")
    phone_number = models.CharField(max_length=12, unique=True)
    email = models.EmailField()
    first_name = None
    last_name = None

    
    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = ['full_name','email']
    objects = UserManager()

    class Meta:
        permissions=[]



# Create your models here.
class Product(models.Model):
    product_name = models.CharField(max_length=50)
    product_logo = models.FileField(upload_to='Product_logo/')
    stock_status = models.BooleanField()
    product_price = models.IntegerField()
    account_type = models.JSONField(default=list)
    validity_in_months = models.JSONField(default=list)
    
    def __str__(self):
        return self.product_name 

