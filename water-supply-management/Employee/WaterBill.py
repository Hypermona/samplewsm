from django.db import models
from .Consumer import Consumer
from .Employee import Employee
from .Ward import Ward


class WaterBill(models.Model):
    bill_id = models.AutoField(primary_key=True)
    ward = models.ForeignKey(Ward, on_delete=models.CASCADE)
    consumer = models.ForeignKey(Consumer, on_delete=models.CASCADE)
    collector = models.ForeignKey(Employee, on_delete=models.CASCADE)
    amount = models.IntegerField()
    is_paid = models.BooleanField()
    read_value = models.IntegerField()
    read_date = models.DateField()
    due_date = models.DateField()
    disconnection_date = models.DateField()

