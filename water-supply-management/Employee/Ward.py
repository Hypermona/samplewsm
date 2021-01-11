from django.db import models
from .Town import Town


class Ward(models.Model):
    ward_id = models.AutoField(primary_key=True)
    town = models.ForeignKey(Town, on_delete=models.CASCADE)
    member_name = models.CharField(max_length=40)
