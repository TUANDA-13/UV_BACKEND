from django.db import models
import uuid
from django.utils import timezone
# Create your models here.


class UV(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    id_esp = models.CharField(max_length=10, editable=True)
    x = models.FloatField(max_length=None, editable=True, default=0)
    y = models.FloatField(max_length=None, editable=True, default=0)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "uvs"
