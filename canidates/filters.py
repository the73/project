import django_filters
from owner.models import Admin

class LocationFilter(django_filters.FilterSet):
    class Meta:
        model= Admin
        fields={"location":["contains"],
                "centers":["contains"],
                "slots":["lt"],
                }