# Generated by Django 5.0.7 on 2024-07-25 09:27

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("Home", "0003_product_account_type"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="validity_in_months",
            field=models.JSONField(default=list),
        ),
    ]
