# Generated by Django 4.1.7 on 2023-03-22 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="CsvFile",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("file", models.FileField(upload_to="data_api/csv_files/")),
                ("description", models.CharField(max_length=255, null=True)),
                ("uploaded_at", models.DateTimeField(auto_now_add=True)),
            ],
            options={
                "verbose_name_plural": "Files",
                "db_table": "Files",
            },
        ),
        migrations.CreateModel(
            name="Purchase",
            fields=[
                ("id", models.IntegerField(primary_key=True, serialize=False)),
                ("order_id", models.IntegerField()),
                ("product", models.CharField(max_length=255)),
                ("quantity_ordered", models.IntegerField()),
                ("price_each", models.DecimalField(decimal_places=2, max_digits=12)),
                ("order_date", models.DateTimeField()),
                ("purchase_adress", models.CharField(max_length=255)),
                ("total", models.DecimalField(decimal_places=2, max_digits=12)),
            ],
            options={
                "db_table": "Purchase",
            },
        ),
    ]
