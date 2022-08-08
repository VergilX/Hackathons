from django.db import models

from users.models import User

# Create your models here.
class Device(models.Model):
    """ Table for list of used codes """

    code = models.CharField(max_length=10, unique=True)
    status = models.BooleanField(default=True, blank=False, null=False)
    user = models.ForeignKey(User, related_name="user", on_delete=models.CASCADE)

    def __str__(self):
        return f"Device code: {self.code}"

    def destroy(self):
        self.delete()
        print("Deleted successfully!")

    def status(self):
        """ Function to display status of device """
        return f"Device(code: {self.code}) status: {self.status}"

class Graph(models.Model):
    """ Database for graphs """

    device = models.ForeignKey(Device, on_delete=models.CASCADE)