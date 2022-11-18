from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.
class MyUserManager(BaseUserManager):
    """
        Class for managing custom user
    """

    def create_user(self, email, username, phone=0, password=None):
        """ Function to create a user """
        if not email:
            raise ValueError("Users must have an email")
        if not username:
            raise ValueError("Users must have a username")

        user = self.model(
            email=self.normalize_email(email),
            username=username,
            phone = phone
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password):
        user = self.create_user(
            email=email,
            username=username,
            password=password
        )

        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser):
    """
    Class for custom user
    """

    name = models.CharField(max_length=60, default="")
    email = models.EmailField(verbose_name="email", max_length=60, unique=True)
    username = models.CharField(max_length=30, unique=True)
    date_joined = models.DateTimeField(verbose_name="date joined", auto_now_add=True)
    last_login = models.DateTimeField(verbose_name="last login", auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    hide_email = models.BooleanField(default=True)

    # custom fields
    is_owner = models.BooleanField(default=False) 

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email", ]

    # using the Manager
    objects = MyUserManager()

    def __str__(self):

        return f"Username: {self.username}"

    def has_perm(self, perm, obj=None):
        """ Has permissions only if admin """
        return self.is_admin
    
    def has_module_perms(self, app_label):
        """ All users have module permissions """

        return True