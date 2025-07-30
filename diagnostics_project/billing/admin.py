from django.contrib import admin
from .models import Patient, Test, Bill

admin.site.register(Patient)
admin.site.register(Test)
admin.site.register(Bill)
