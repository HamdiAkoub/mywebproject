import uuid
from django.db import models

class TBL000(models.Model):
    cardguide = models.UUIDField(db_column='cardguide', primary_key=True, default=uuid.uuid4)
    mainguide = models.
