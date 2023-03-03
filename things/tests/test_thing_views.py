from django.test import TestCase
from django.urls import reverse, reverse_lazy

from things.forms import ThingForm
from things.models import Thing
from things.views import ThingFormView, ThingListView


THING_LIST_URL = '/things/'
THING_LIST_VIEW_NAME = 'things:list'
THING_LIST_TEMPLATE = 'things/thing_list.html'

THING_FORM_URL = '/things/form/'
THING_FORM_VIEW_NAME = 'things:form'
THING_FORM_TEMPLATE = 'things/thing_form.html'


class ThingListViewTest(TestCase):
    """
    Test the `ThingListView`.
    """
    
    def test_thing_list_view_url_exists_at_desired_location(self):
        """
        Test that the `ThingListView` URL exists at the desired location.
        """
        response = self.client.get(THING_LIST_URL)
        self.assertEqual(response.status_code, 200)

    def test_thing_list_view_url_accessible_by_name(self):
        """
        Test that the `ThingListView` URL is accessible by name.
        """
        response = self.client.get(reverse(THING_LIST_VIEW_NAME))
        self.assertEqual(response.status_code, 200)

    def test_thing_list_view_uses_correct_template(self):
        """
        Test that the `ThingListView` uses the correct template.
        """
        response = self.client.get(reverse('things:list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, THING_LIST_TEMPLATE)

    def test_thing_list_view_displays_all_things(self):
        """
        Test that the `ThingListView` displays all `Thing` objects.
        """
        # Create two `Thing` objects.
        thing1 = Thing.objects.create(name='Thing 1')
        thing2 = Thing.objects.create(name='Thing 2')
        # Get the response from the `ThingListView`.
        response = self.client.get(THING_LIST_URL)
        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 200)
        # Check that the response contains the two `Thing` objects.
        self.assertContains(response, thing1.name)
        self.assertContains(response, thing2.name)

        ################################################################
        ### Code created by GitHub Copilot. Not working as expected. ###
        # self.assertQuerysetEqual(
        #     response.context['object_list'],
        #     ['<Thing: Thing 1>', '<Thing: Thing 2>'],
        #     ordered=False
        # )
        ################################################################
