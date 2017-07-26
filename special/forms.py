from dal import autocomplete
from django import forms

from cards.models import Card
from special.models import Special


class SpecialForm(forms.ModelForm):
    card_id = forms.ChoiceField(
        choices=[],  # TODO: fill thise up
        widget=autocomplete.Select2(url='special:autocomplete')
    )

    class Meta:
        model = Special
        fields = ('__all__')
