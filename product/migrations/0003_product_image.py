# Generated by Django 3.0.8 on 2020-07-13 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_auto_20200713_1430'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='product_images', verbose_name='Изображение товара'),
        ),
    ]
