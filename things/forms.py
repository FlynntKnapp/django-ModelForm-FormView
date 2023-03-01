from django.forms import ModelForm, ValidationError

from things.models import Thing


class ThingForm(ModelForm):
    class Meta:
        model = Thing
        fields = ['name']

    def clean_name(self):
        name = self.cleaned_data['name']
        if len(name) < 3:
            raise ValidationError('Name must be at least 3 characters long.')
        return name

    # def save(self, commit=True):
    #     thing = super().save(commit=False)
    #     if commit:
    #         thing.save()
    #     return thing
