from rest_framework.views import APIView
from rest_framework.response import Response
from common.utils import get_paginated_data
from .models import Product
from .serializers import ProductListSerializer
from .paginations import ProductListPagination


class ProductHomeAPI(APIView):
    def get(self, request):
        """
        Devuelve los 8 productos más recientes
        """

        products = Product.objects.all().order_by("-created_at")[:8]
        serializer = ProductListSerializer(products, many=True)
        return Response(data=serializer.data)


class ProductListAPI(APIView):
    def get(self, request):
        """
        Devuelve la lista de productos páginados
        """
        products = Product.objects.all()

        return get_paginated_data(
            pagination_class=ProductListPagination,
            request=request,
            serializer_class=ProductListSerializer,
            queryset=products,
        )
