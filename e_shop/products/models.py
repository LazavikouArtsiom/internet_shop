from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from orders.models import Cart

class Sale(models.Model):
    name = models.CharField(max_length=150)
    description = models.CharField(max_length=255)
    percent = models.IntegerField(verbose_name='Процент')

    class Meta:
        ordering = ('name', 'percent')
        verbose_name = 'Скидка'
        verbose_name_plural = 'Скидки'

    def __str__(self):
        return self.name + ' ' + str(self.percent)

class Manufacturer(models.Model):
    name = models.CharField(max_length=255, verbose_name='Производитель', null=True, blank=True)
    country = models.CharField(max_length=150, verbose_name='Страна производитель', null=True, blank=True)

    class Meta:
        ordering = ('name','country')
        verbose_name = 'Производитель'
        verbose_name_plural = 'Производители'

    def __str__(self):
        return self.name

class Attribute(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    
    class Meta:
        ordering = ('name',)
        verbose_name = 'Характеристика'
        verbose_name_plural = 'Характеристики'

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, db_index=True)
    parental_category = models.ManyToManyField('self', 
                                                blank=True,
                                                verbose_name='Категория-родитель',
                                                )
    
    class Meta:
        ordering = ('name',)
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name
    



class Product(models.Model):
    name = models.CharField(max_length=150, db_index=True,
                            verbose_name='Название')
    slug = models.SlugField(max_length=150, db_index=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, 
                                verbose_name='Цена')
    category = models.ForeignKey(Category, 
                                 related_name='category',
                                 null=True,
                                 blank=True,
                                 verbose_name='Категория',
                                 on_delete=models.SET_NULL,
                                 )
    manufacturer = models.ForeignKey(Manufacturer,
                                     related_name='manufacturer', 
                                     null=True,
                                     blank=True,
                                     verbose_name='Производитель',
                                     on_delete=models.SET_NULL)
    sales = models.ManyToManyField(Sale, 
                                   related_name='sales',
                                   verbose_name='Скидка',
                                   )
    attributes = models.ManyToManyField(Attribute, 
                                        related_name='attributes', 
                                        through='ProductAttribute')
    carts = models.ManyToManyField(Cart, 
                                   related_name='carts', 
                                   through='CartItems')
    image = models.CharField(max_length=255, blank=True, 
                             verbose_name='Картинка')
    available = models.BooleanField(default=True, verbose_name='В наличии')
    stock = models.PositiveIntegerField(verbose_name='На складе')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Создан')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Обновлён')

    class Meta:
        ordering = ('name', 'created_at',)
        index_together = ('id', 'slug')
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return self.name

class ProductAttribute(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    attribute = models.ForeignKey(Attribute, null=True ,on_delete=models.SET_NULL)
    value = models.CharField(max_length=255)
    
    class Meta:
        verbose_name = 'Продукт - Характеристика'

    def __str__(self):
        return self.product.name + ' : ' + self.attribute.name + ' - ' + self.value

class CartItems(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(default=1)
    total_price = models.IntegerField(default=0)

    def __str__(self):
        return f'Cart id {self.cart.id} --- product {self.product.name} amount {str(self.quantity)}' 
 