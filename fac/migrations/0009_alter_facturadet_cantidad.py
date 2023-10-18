# Generated by Django 4.1.5 on 2023-10-14 23:06

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("fac", "0008_facturaenc_estado_fel"),
    ]

    operations = [
        migrations.AlterField(
            model_name="facturadet",
            name="cantidad",
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=18),
        ),
    ]
