from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from phonenumber_field.modelfields import PhoneNumberField

# Note: Commented things are stuff I don't understand

# Create your models here.
class Language(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return f"Language: {self.name}"

class Certificate(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return f"Certificate: {self.name}"

class Skill(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return f"Skill: {self.name}"

class Club(models.Model):
    name = models.CharField(max_length=30)
    members = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return f"Club {self.name}"

class Referee(models.Model):
    name = models.CharField(max_length=60)
    position = models.CharField(max_length=10)
    job = models.CharField(max_length=30)
    phone = PhoneNumberField(blank=True, null=True, unique=True)
    description = models.CharField(max_length=100)

    def __str__(self):
        return f"Referee: {self.name}"

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

    # personal fields
    certificates = models.ManyToManyField(Certificate, related_name="users")
    skills = models.ManyToManyField(Skill, related_name="users")
    address = models.CharField(max_length=100, default="")
    phone = PhoneNumberField(blank=True, null=True, unique=True)
    lang = models.ManyToManyField(Language, related_name="users")
    clubs = models.ManyToManyField(Club, related_name="memebers")
    summary = models.CharField(max_length=100, default="")
    references = models.ManyToManyField(Referee, related_name="candidates")

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
class Education(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="student")
    qualification = models.CharField(max_length=5)
    institution = models.CharField(max_length=30)
    description = models.CharField(max_length=100, default="")
    start_year = models.IntegerField(blank=False, null=False)
    end_year = models.IntegerField(blank=False, null=False)

    def __str__(self):
        return f"Education of {self.user}"

    def main(self):
        """ Returns main components in form: "<Degree>, <institution> """

        return f"{self.qualification}, {self.institution}"

    def returnperiod(self):
        """ Returns education period in format yyyy-yy """

        return f"{self.start_year}-{self.end_year % 100}"

class WorkExperience(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="employee")
    job = models.CharField(max_length=30)
    company = models.CharField(max_length=20)
    description = models.CharField(max_length=100)
    start_year = models.IntegerField(blank=False, null=False)
    end_year = models.IntegerField(blank=False, null=False)

    def __str__(self):
        return f"Work Experience of {self.user}"

    def main(self):
        """ Returns main components in form: "<Degree>, <institution> """

        return f"{self.job}, {self.company}"

    def returnperiod(self):
        """ Returns education period in format yyyy-yy """

        return f"{self.start_year}-{self.end_year % 100}"