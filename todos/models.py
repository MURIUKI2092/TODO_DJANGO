from django.db import models
from helpers.models import TrackingModel
from authentication.models import User
import uuid
# Create your models here.

class Todo(TrackingModel):
    todo_uuid =models.UUIDField(default=uuid.uuid4, editable=False,unique=True)
    title = models.TextField()
    description = models.TextField()
    is_complete = models.BooleanField(default=False)
    owner =models.ForeignKey(to=User,on_delete=models.CASCADE) 
    
    def __str__(self):
        return self.title