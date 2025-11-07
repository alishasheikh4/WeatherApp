from django.db import models

class Weather(models.Model):
    city = models.CharField(max_length=100)
    temperature = models.FloatField()
    description = models.CharField(max_length=200)
    country = models.CharField(max_length=100, blank=True, null=True)
    icon = models.CharField(max_length=10, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.city} - {self.temperature}°C"
