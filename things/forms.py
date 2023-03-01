from django.forms import ModelForm

from things.models import Thing


class ThingForm(ModelForm):
    class Meta:
        model = Thing
        # We can specify any/all/__all__ of the `Thing` model's fields here:
        fields = [
            'name'
        ]
