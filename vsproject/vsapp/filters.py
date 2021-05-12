from .models import Movies
import django_filters
from django_filters.filters import RangeFilter

# Creating movie filters

class MoviesFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')
    price = RangeFilter()

    class Meta:
        model = Movies
        fields = ['name','price']