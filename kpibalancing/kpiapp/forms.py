from django import forms
from django.core.exceptions import ValidationError

from .models import *
from django.forms import modelformset_factory


class CardsForm(forms.ModelForm):

    def clean(self):
        cleaned_data = super().clean()
        post_weight = cleaned_data.get("weight")
        post_method = cleaned_data.get("method")
        if post_method == 3:
            if post_weight > 0:
                raise ValidationError(
                    "invalid"
                )
        else:
            if post_weight < 9 or post_weight > 61:
                # Only do something if both fields are valid so far.
                raise ValidationError(
                    "weight must be between 10 and 60"
                )
            if post_method == 0 or post_method == 1:
                if post_weight % 5 != 0:
                    raise ValidationError("invalid")


    class Meta:
        model = Card

        fields = [
            'organization',
            'role',
            'fio',
            'id_kpi_record',
            'name',
            'method',
            'low_level',
            'target_level',
            'high_level',
            'weight',
        ]


CardFormSet = modelformset_factory(
    Card, fields=('organization', 'role', 'fio',
                  'name', 'method',
                  'low_level', 'target_level', 'high_level',
                  'weight'), extra=1
)