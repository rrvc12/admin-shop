from django.contrib import admin
from .models import Category, Product
# Register your models here.


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "slug",
        "parent",
        "created_at",
        "updated_at",
    )
    search_fields = ("name", "slug")
    list_filter = ("created_at", "updated_at")


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "slug",
        "category",
        "sale_price",
        "created_at",
        "updated_at",
    )
    search_fields = ("name", "slug")
    list_filter = ("created_at", "updated_at", "category")
