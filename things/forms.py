from django.forms import ModelForm

from things.models import Thing


class ThingForm(ModelForm):
    """
    Form for a user to create a new `Thing`.

    This form inherits the `ModelForm` class from Django's forms.
    `ModelForm` inherits from `BaseModelForm`.
    `BaseModelForm` inherits from `BaseForm`.
    """
    class Meta:
        model = Thing
        # We can specify any/all/__all__ of the `Thing` model's fields here:
        fields = [
            'name'
        ]
