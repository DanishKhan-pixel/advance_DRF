from django.contrib import admin

# Register your models here.

from .models import Transactions
from .models import people

admin.site.register(Transactions)
admin.site.register(people)