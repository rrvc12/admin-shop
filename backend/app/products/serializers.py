from rest_framework import serializers


class CategoryNestedSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    slug = serializers.CharField()


class CategoryDetailSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    description = serializers.CharField()
    slug = serializers.CharField()
    parent = CategoryNestedSerializer(
        allow_null=True,
    )


class ProductNestedSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    slug = serializers.CharField()


class ProductDetailSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    description = serializers.CharField()
    category = CategoryNestedSerializer(
        allow_null=True,
    )
    image_url = serializers.CharField()
    slug = serializers.CharField()
    sale_price = serializers.DecimalField(
        max_digits=10,
        decimal_places=2,
    )


class ProductListSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    image_url = serializers.CharField()
    slug = serializers.CharField()
    sale_price = serializers.DecimalField(
        max_digits=10,
        decimal_places=2,
    )
