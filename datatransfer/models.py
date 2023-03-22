from django.db import models


class Purchase(models.Model):

    id = models.IntegerField(primary_key=True, auto_created=True)
    order_id = models.IntegerField(null=False)
    product = models.CharField(max_length=255)
    quantity_ordered = models.IntegerField(null=False)
    price_each = models.DecimalField(max_digits=12, decimal_places=2)
    order_date = models.DateTimeField(null=False)
    purchase_adress = models.CharField(max_length=255)
    total = models.DecimalField(max_digits=12, decimal_places=2)

    class Meta:
        db_table = 'Purchase'


class CsvFile(models.Model):
    file = models.FileField(blank=False, null=False, upload_to='data_api/csv_files/')
    description = models.CharField(max_length=255, null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'Files'
        verbose_name_plural = 'Files'

