# Generated by Django 3.0.8 on 2020-09-30 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0006_product_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='deleted',
            field=models.BooleanField(default=False),
        ),
    ]
