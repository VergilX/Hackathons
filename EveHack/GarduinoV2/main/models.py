from django.db import models

# Create your models here.

class PlantData(models.Model):

    # Different model statuses of plant
    PLANT_STATUS = [
        ("H", "Healthy"),
        ("I", "Infected"),
        ("W", "Withered"),
        ("N", "No stats available"),
    ]

    # All required data from plant
    name = models.CharField(max_length=50, default="Not set")
    temp = models.FloatField(default=0.0)
    humidity = models.FloatField(default=0.0)
    next_spray = models.TimeField()
    fertilizer_level = models.FloatField(default=0.0)
    led_intensity = models.FloatField(default=0.0)
    time_to_sundown = models.TimeField()
    status = models.CharField(max_length=1, choices=PLANT_STATUS, default="N")

    def __str__(self):
        return f"Plant: {self.name}"