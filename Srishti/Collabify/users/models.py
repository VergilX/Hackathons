from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Note: Commented things are stuff I don't understand

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
        user.save(using=self._db)
        return user

"""
def get_profile_image_filepath(self):
    ''' The profile images will be saved in the below path 
    
    All uploaded images will be stored with name 'profile_image.png' '''

    return f'profile_images/{self.pk}/{"profile_image.png"}'

def get_default_profile_image():

    # return the default image file path
    return 
"""

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
    # profile_image = models.ImageField(max_length=255, upload_to=, null=True, blank=True, default=)
    hide_email = models.BooleanField(default=True)

    # these must match the variables used in definition
    USERNAME_FIELD = "username" # The base field which is needed to create user
    REQUIRED_FIELDS = ["email", ] # Custom required fields

    # Telling it how to use the manager
    objects = MyUserManager()

    def __str__(self):
        """ A default thing that appears when no field is accessed """

        return f"Username: {self.username}"

    # default functions required by django to create user
    def has_perm(self, perm, obj=None):
        """ Has permissions only if admin. Default = false """
        return self.is_admin

    def has_module_perms(self, app_label):
        """ All users have module permissions """
        return True

"""
    # other functions
    def get_profile_image_filename(self):
        ''' This function extracts the filename of the uploaded profile picture 
        
        Check out the path in get_profile_image_filepath function '''

        # This is basically substringing. Look carefully
        return str(self.profile_image)[str(self.profile_image).index(f'profile_images/{self.pk}/'):]
"""