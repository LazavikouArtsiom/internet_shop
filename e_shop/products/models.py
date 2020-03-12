from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from orders.models import Order

class Sale(models.Model):
    name = models.CharField(max_length=150)
    description = models.CharField(max_length=255)
    percent = models.IntegerField(verbose_name='Процент')
    
    def __str__(self):
        return str(self.percent)

class Manufacturer(models.Model):
    name = models.CharField(max_length=255, verbose_name='Производитель', null=True)
    country = models.CharField(max_length=150, verbose_name='Страна производитель', null=True)

    def __str__(self):
        return self.name

class Attribute(models.Model):
    name = models.CharField(max_length=255, verbose_name='Атрибут' , null=True)
    
    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name='Категория')
    parental_category = models.ManyToManyField('self', blank=True, verbose_name='Категория-родитель')

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название продукта')
    price = models.FloatField(validators=[MinValueValidator(0.0)], verbose_name='Цена')
    manufacturer = models.ForeignKey(Manufacturer, null=True, on_delete=models.SET_NULL)
    sale = models.ManyToManyField(Sale, verbose_name='Скидка', related_name='sale', blank=True)
    category = models.ManyToManyField(Category, verbose_name='Категория', related_name='category', blank=True)
    attribute = models.ManyToManyField(Attribute, verbose_name='Характеристика', related_name='attribute', through='ProductAttribute')
    order = models.ManyToManyField(Order, verbose_name='Заказ', related_name='order', through='Cart')


    def __str__(self):
        return self.name


class ProductAttribute(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    attribute = models.ForeignKey(Attribute, null=True ,on_delete=models.SET_NULL)
    value = models.CharField(max_length=255)

    def __str__(self):
        return self.product.name + ' : ' + self.attribute.name + ' - ' + self.value

class Cart(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(default=1)
    total_price = models.IntegerField(default=0)

    def __str__(self):
        return f'order id {self.order.id} --- product {self.product.name} amount {str(self.quantity)}' 
 