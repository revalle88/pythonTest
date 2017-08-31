from django.contrib import admin
from .models import Person
from .models import Department
# Register your models here.

admin.site.register(Department)
admin.site.register(Person)