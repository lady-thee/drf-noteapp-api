from django.db import models
import uuid 


class Notes(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, unique=True)
    title = models.CharField(max_length=200, blank=True, null=True)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True, blank=True, null=True)


    class Meta:
        ordering = ['id']
