from rest_framework.pagination import PageNumberPagination


class NetElementPagination(PageNumberPagination):
    """
    Пагинатор для вывода 10 элементов сети на каждой странице
    """
    page_size = 10
