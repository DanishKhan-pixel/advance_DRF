from django.contrib import admin

# Register your models here.

from .models import Transations
from .models import people

admin.site.register(Transations)
admin.site.register(people)