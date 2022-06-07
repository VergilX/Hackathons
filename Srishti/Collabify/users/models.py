from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.
# Class required: for managing users
class MyUserManager(BaseUserManager):

    # required functions by django
    def create_user(self, email, username, password=None):
        """ Function to create a user. Add fields which are required as parameters """
        if not email:
            # If user hasn't provided email
            raise ValueError("Users must have an email")
        if not username:
            raise ValueError("User must have a username")
        
        # Add more fields if needed, if all are satisfied:
        user = self.model(
            email=self.normalize_email(email), # normailze_email converts to lower case (it's in BaseUserManager clasds)
            username=username,
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

        # removing defaults of User class (check definition)
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(usingi=self._db)
        return user

# Class for custom user
class User(AbstractBaseUser):
    # Required by django for making a custom user
    email = models.EmailField(verbose_name="email", max_length=60, unique=True)
    username = models.CharField(max_length=30, unique=True)
    date_joined = models.DateTimeField(verbose_name="date joined", auto_now_add=True)
    last_login = models.DateTimeField(verbose_name="last login", auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    # add custom fields

    USERNAME_FIELD = "username" # The base field which is needed to create user
    REQUIRED_FIELD = ["email", ] # Custom required fields

    # Telling it how to use the manager
    objects = MyUserManager()

    def __str__(self):
        return f"Username: {self.username}; Email: {self.email}"

    # default functions required by django to create user
    def has_perm(self, perm, obj=None):
        """ Has permissions only if admin. Default = false """
        return self.is_admin

    def has_module_perms(self, app_label):
        """ All users have module permissions """
        return True