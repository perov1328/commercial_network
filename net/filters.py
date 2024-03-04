from django_filters import rest_framework as filters
from net.models import NetElement


class NetElementFilter(filters.FilterSet):
    country = filters.CharFilter(field_name='country', lookup_expr='icontains')

    class Meta:
        model = NetElement
        fields = ['country']
