from django.db import models

class HushemPrediction(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    results = models.CharField(max_length=50, null=True, blank=True)
    precision = models.FloatField(null=True, blank=True)
