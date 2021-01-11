from django.db import models
from .Consumer import Consumer


class Complaint(models.Model):
    complaint_id = models.AutoField(primary_key=True)
    consumer = models.ForeignKey(Consumer, on_delete=models.CASCADE)
    complaint_data = models.TextField()
