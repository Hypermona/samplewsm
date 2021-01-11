from django.db import models
from .Employee import Employee
from .Ward import Ward


class Meter(models):
    meter_id = models.AutoField(primary_key=True)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    ward = models.ForeignKey(Ward, on_delete=models.CASCADE)
    HEALTH = (
        ('G', 'GOOD'),
        ('O', 'OK'),
        ('B', 'BAD'),
    )
    meter_health = models.CharField(max_length=10, choices=HEALTH, null=True)
