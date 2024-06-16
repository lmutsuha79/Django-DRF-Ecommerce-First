from django.db import models
from mptt.models import MPTTModel, TreeForeignKey


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    brand = models.ForeignKey('Brand', on_delete=models.PROTECT, null=True)
    category = TreeForeignKey('Category', on_delete=models.PROTECT, null=True)
    is_digital = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Brand(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Category(MPTTModel):
    name = models.CharField(max_length=100)
    # so you need to delete all the subcategories before deleting the parent category
    # or the operation will be prevented by the on_delete=models.PROTECT
    parent = TreeForeignKey('self', on_delete=models.PROTECT, null=True, blank=True)

    class MPTTMeta:
        order_insertion_by = ['name']

    def __str__(self):
        return self.name
