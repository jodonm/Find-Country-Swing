from django.db import models
import pandas as pd


class Spot(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    address = models.TextField()
    STATUS_CHOICES = (
        ('pending', 'Pending Review'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    )
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')

    def __str__(self):
        return self.name
    


