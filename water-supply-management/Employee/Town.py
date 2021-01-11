from django.db import models


class Town(models.Model):
    town_id = models.AutoField(primary_key=True)
    location = models.CharField()
