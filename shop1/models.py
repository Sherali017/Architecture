from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class CategoryModel(models.Model):
    title = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'


class AuthorModel(models.Model):
    name = models.CharField(max_length=255)
    avatar = models.ImageField(upload_to='products')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'author'
        verbose_name_plural = 'authors'


class ProductModel(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='products')
    price = models.FloatField()
    real_price = models.FloatField()
    discount = models.PositiveIntegerField(
        default=0,
        validators=[
            MinValueValidator(0),
            MaxValueValidator(100)

        ])
    category = models.ForeignKey(CategoryModel, on_delete=models.CASCADE, related_name='products')
    author = models.ForeignKey(AuthorModel, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)

    def is_discount(self):
        return self.discount != 0

    def get_price(self):
        if self.is_discount():
            return self.price - self.price * self.discount / 100
        return self.price

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'product'
        verbose_name_plural = 'products'


from django.db import models

# Create your models here.
