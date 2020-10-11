from django.contrib import admin

# Register your models here.

from .models import Items, Ordered_item

admin.site.register(Items)
admin.site.register(Ordered_item)