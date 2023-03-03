from django.test import TestCase

from things.forms import ThingForm
from things.models import Thing


class ThingFormTest(TestCase):
    """
    Test the `ThingForm`.
    """

    def test_thing_form_has_correct_model(self):
        """
        Test that the form has the correct model.
        """
        form = ThingForm()
        self.assertEqual(form.Meta.model, Thing)
    
    def test_thing_form_has_correct_fields(self):
        """
        Test that the form has the correct fields.
        """
        form = ThingForm()
        self.assertEqual(form.Meta.fields, ['name'])
    
    # def test_thing_form_field_labels(self):
    #     """Test that the form has the correct field labels."""
    #     form = ThingForm()
    #     self.assertTrue(
    #         form.fields['name'].label is None or
    #         form.fields['name'].label == 'Thing Name'
    #     )

    # def test_thing_form_field_help_texts(self):
    #     """Test that the form has the correct field help texts."""
    #     form = ThingForm()
    #     self.assertEqual(
    #         form.fields['name'].help_text,
    #         'Enter a name for the thing.'
    #     )

    # def test_thing_form_field_required(self):
    #     """Test that the form has the correct field required attributes."""
    #     form = ThingForm()
    #     self.assertTrue(form.fields['name'].required)
