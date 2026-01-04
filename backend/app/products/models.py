from django.db import models
from common.models import BaseModal
from django.conf import settings


class Category(BaseModal):
    name = models.CharField(
        null=True,
        blank=True,
        max_length=100,
    )

    description = models.TextField(
        null=True,
        blank=True,
    )

    slug = models.SlugField(
        unique=True,
    )

    parent = models.ForeignKey(
        to="self",
        on_delete=models.RESTRICT,
        related_name="childrens",
        null=True,
        blank=True,
    )

    class Meta:
        ordering = ["name"]
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self.generate_unique_slug()
        super().save(*args, **kwargs)


class Product(BaseModal):
    name = models.CharField(
        null=True,
        blank=True,
        max_length=100,
    )

    description = models.TextField(
        null=True,
        blank=True,
    )

    category = models.ForeignKey(
        to="products.Category",
        on_delete=models.SET_NULL,
        related_name="products",
        null=True,
        blank=True,
    )

    image = models.FileField(
        upload_to="products",
        blank=True,
        null=True,
    )

    slug = models.SlugField(
        null=True,
        blank=True,
        unique=True,
    )

    sale_price = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=0.00,
        null=True,
        blank=True,
    )

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name

    def image_url(self):
        if not self.image:
            return None
        return f"{settings.BACKEND_URL}{self.image.url}"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self.generate_unique_slug()
        super().save(*args, **kwargs)
