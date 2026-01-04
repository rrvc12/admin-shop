from rest_framework.pagination import PageNumberPagination


class BasePagePagination(PageNumberPagination):
    page_size = 20  # Número por defecto

    def get_paginated_response(self, data):
        """
        Añadimos el total de páginas a la respuesta
        """
        res = super().get_paginated_response(data)
        res.data["num_pages"] = self.page.paginator.num_pages
        return res
