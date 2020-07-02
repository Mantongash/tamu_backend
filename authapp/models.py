from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
  REQUIRED_FIELDS = ['first_name','last_name', 'email', 'password']
  USERNAME_FIELD = 'username'

  def get_username(self):
    return self.username
