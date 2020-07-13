# Generated by Django 3.0.8 on 2020-07-13 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('price', models.DecimalField(decimal_places=3, max_digits=11, verbose_name='Цена')),
                ('salse', models.IntegerField(default=0, verbose_name='Кол-во продаж')),
                ('aviable', models.BooleanField(default=True, verbose_name='Есть в наличии')),
            ],
            options={
                'verbose_name': 'Товар',
                'verbose_name_plural': 'Товары',
            },
        ),
    ]
