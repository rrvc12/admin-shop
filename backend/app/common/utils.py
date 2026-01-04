from rest_framework.response import Response
from .pagination import BasePagePagination


def get_paginated_data(request, serializer, queryset, pagination_class=None):
    """
    Recibe los datos serializados y devuelve la respuesta paginada
    """

    if pagination_class is None:
        pagination_class = BasePagePagination
    paginator = pagination_class()

    paginate_queryset = paginator.paginate_queryset(queryset, request)

    if paginate_queryset is not None:
        # Devuelve la respuesta paginada
        return paginator.get_paginated_response(serializer.data)

    # Devuelve todos los elementos sin paginar
    return Response(data=serializer.data)
