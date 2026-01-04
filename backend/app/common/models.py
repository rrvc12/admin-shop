from django.db import models
from uuid import uuid4
from django.utils.text import slugify


# Create your models here.
class BaseModal(models.Model):
    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    updated_at = models.DateTimeField(
        auto_now=True,
    )

    def generate_unique_slug(self, name_field="name"):
        slug = slugify(getattr(self, name_field))
        unique_slug = slug
        while self.__class__.objects.filter(slug=unique_slug).exists():
            unique_slug = f"{slug}-{uuid4().hex[:6]}"
        return unique_slug

    class Meta:
        abstract = True
