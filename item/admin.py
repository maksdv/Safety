from django.contrib import admin
from .models import Chair
from .models import Item

admin.site.register(Chair)
admin.site.register(Item)