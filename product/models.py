from django.db import models
from django.contrib.auth.models import User 
# Create your models here.

class Product(models.Model):
    name = models.CharField(
        max_length = 255 , verbose_name = "Название")

    user = models.ForeignKey(
        to=User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="product",
        verbose_name="Продавец"
    )

    category = models.ForeignKey(
        "Category" , 
        on_delete = models.SET_NULL,
        related_name = "product",
        null = True ,
        blank = True,
        verbose_name = "Категория")

    image = models.ImageField(
        null = True ,
        blank = True ,
        upload_to = "product_images" ,
        verbose_name="Изображение товара",
        default="static/no_image.png"
    )

    description =models.TextField(
        null = True , blank = True ,verbose_name = "Описание")
 
    price = models.DecimalField(
        max_digits = 11,
        decimal_places = 3,
        verbose_name = "Цена")

    salse =models.IntegerField(
        default = 0 , verbose_name = "Кол-во продаж")

    available = models.BooleanField(
        default = True, verbose_name = "Есть в наличии")

    deleted = models.BooleanField(
        default=False,
        verbose_name="Удалено"
        )

    def __str__(self):
        return self.name 

    class Meta:
        verbose_name = "товар"
        verbose_name_plural = "Товары"


class Category(models.Model):
    name = models.CharField(
        max_length = 250 , verbose_name = "Название")

    def __str__(self):
        return self.name

    class Meta :
        verbose_name = "категория"
        verbose_name_plural = "Категории"
