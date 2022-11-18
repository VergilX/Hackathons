from django.db import models

from users.models import User

# Create your models here.
class Location(models.Model):
    name = models.CharField(max_length=100, default="")

    def __str__(self):
        return f"Location: {self.name}"

class Buyers(models.Model):
    username = models.ForeignKey(User, related_name="buyer_model", default="", on_delete=models.PROTECT)
    location = models.ForeignKey(Location, related_name="buyer_locations", on_delete=models.PROTECT)
    
    def __str__(self):
        return f"Buyer username: {self.username}"

    def destroy(self):
        self.delete()
        print("Deleted successfully!")

class Sellers(models.Model):
    username = models.ForeignKey(User, related_name="seller_model", default="", on_delete=models.PROTECT)
    shop_name = models.CharField(max_length=100, default="")
    shop_location = models.ForeignKey(Location, related_name="shops", on_delete=models.PROTECT)

    def __str__(self):
        return f"Shop: {self.name}"

    def get_location(self):
        return f"Location: {self.shop_location}"

    def destroy(self):
        self.delete()
        print("Deleted successfully!")

class ItemList(models.Model):
    name = models.CharField(max_length=100, default="")
    shops = models.ManyToManyField(Sellers, related_name="items")

    def __str__(self):
        return f"Item: {self.name}"
    