import django_filters

from .models import *


class CardFilter(django_filters.FilterSet):
    class Meta:
        model = Card
        fields = ['user', 'organization','function',
                  'type', 'action', 'id_worker',
                  'role', 'fio',
                  'name', 'method', 'low_level',
                  'target_level', 'high_level',
                  'weight']