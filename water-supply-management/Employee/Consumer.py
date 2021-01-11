from django.db import models


class Consumer(models.Model):
    client_id = models.CharField(max_length=30, primary_key=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email_id = models.EmailField()
    password = models.CharField(max_length=200, )
    dob = models.DateField(null=True)
    # age = models.IntegerField()
    address = models.TextField(max_length=250, null=True)
    GENDER = (
        ('M', 'MALE'),
        ('F', 'FEMALE'),
        ('N', 'NOTAPPLICABEL'),
    )
    gender = models.CharField(max_length=10, choices=GENDER, null=True)

    def __str__(self):
        return self.client_id

    @staticmethod
    def get_all_employees():
        return Consumer.objects.all()

    @staticmethod
    def get_consumer_by_username(username):
        print(username)
        try:
            return Consumer.objects.get(client_id=username)
        except:
            return False

    def register(self):
        self.save()
