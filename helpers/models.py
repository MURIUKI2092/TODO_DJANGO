from django.db import models
import uuid

class TrackingModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now=True)
    
    class Meta:
        abstract = True
        ordering =("-created_at",)