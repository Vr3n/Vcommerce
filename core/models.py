from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

# Create your models here.


class Category(models.Model):
    name = models.CharField(verbose_name=('Category name'), max_length=250)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["name"]
        verbose_name_plural = "Categories"

    def get_absolute_url(self):
        return reverse('category', kwargs={'pk': self.pk})

    def __str__(self) -> str:
        return f"{self.name}"


class Product(models.Model):
    name = models.CharField(verbose_name=(_('Product Name')), max_length=250)
    price = models.DecimalField(verbose_name=(
        _('Price')), max_digits=6, decimal_places=2)
    description = models.TextField(
        verbose_name=(_('Description')), max_length=250)
    image_url = models.URLField(null=True, blank=True)
    category = models.ManyToManyField(Category)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_on']

    def get_absolute_url(self):
        return reverse('product', kwargs={'pk': self.pk})

    def __str__(self) -> str:
        return f"{self.name} - {self.price}"
