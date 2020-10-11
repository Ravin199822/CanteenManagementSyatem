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


class Users(models.Model):
    enrollment_no = models.CharField(max_length=20)
    user_name = models.CharField(max_length=100)
    contact_no = models.CharField(max_length=20)

    def __str__(self):
        return self.user_name

    class Meta:
        db_table = "users"


class Ordered_item(models.Model):
    identity = models.CharField(max_length=20)
    prefered_menu = models.CharField(max_length=20)
    ordered_items = models.CharField(max_length=500)
    total_amount = models.CharField(max_length=20)
    contact_no = models.CharField(max_length=20)
    payment_status = models.CharField(max_length=10, default="false")
    order_status = models.CharField(max_length=10, default="unserved")
    def __str__(self):
        return self.ordered_items

    class Meta:
        db_table = "ordered_item"