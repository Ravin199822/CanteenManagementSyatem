from django.db import models


# Create your models here.

class Items(models.Model):
    item_id = models.CharField(max_length=20)
    category = models.CharField(max_length=40)
    name = models.CharField(max_length=100)
    price = models.CharField(max_length=10)
    desc = models.CharField(max_length=250)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "items"


