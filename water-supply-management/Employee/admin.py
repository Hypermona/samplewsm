from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models.Employee import Employee
from .models.Consumer import Consumer
from .models.Complaint import Complaint


# Register your models here.
# class AdminEmployee(admin.UserAdmin):
#     list_display = ['employee_id', 'first_name', 'last_name', 'email_id', 'dob', 'salary', 'address', 'gender']

class AdminEmployee(admin.ModelAdmin):
    list_display = ['employee_id', 'first_name', 'last_name', 'email_id', 'dob', 'salary', 'address', 'gender', ]


class AdminConsumer(admin.ModelAdmin):
    list_display = ['client_id', 'first_name', 'last_name', 'email_id', 'dob', 'address', 'gender', ]


class AdminComplaint(admin.ModelAdmin):
    list_display = ['consumer', 'complaint_data']


admin.site.register(Employee, AdminEmployee)
admin.site.register(Consumer, AdminConsumer)
admin.site.register(Complaint, AdminComplaint)
