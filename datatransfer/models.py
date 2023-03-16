from django.db import models


class Purchase(models.Model):

    order_id = models.IntegerField(null=False)
    product = models.CharField(max_length=255)
    quantity_ordered = models.IntegerField(null=False)
    price_each = models.DecimalField(max_digits=12, decimal_places=2)
    order_date = models.DateTimeField(null=False)
    purchase_adress = models.CharField(max_length=255)
    total = models.DecimalField(max_digits=12, decimal_places=2)

    class Meta:
        db_table = 'Purchase'
