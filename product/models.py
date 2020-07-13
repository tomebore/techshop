from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(
        max_length = 255 , verbose_name = "Название")

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
        verbose_name = "Изображение товара",
    )

    description =models.TextField(
        null = True , blank = True ,verbose_name = "Описание")
 
    price = models.DecimalField(
        max_digits = 11,
        decimal_places = 3,
        verbose_name = "Цена")

    salse =models.IntegerField(
        default = 0 , verbose_name = "Кол-во продаж")

    aviable = models.BooleanField(
        default = True, verbose_name = "Есть в наличии")



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
