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
    
    def test_thing_list_view_accessible_at_proper_url(self):
        """
        `ThingListView` should be accessible at `THING_LIST_URL`.
        """
        response = self.client.get(THING_LIST_URL)
        self.assertEqual(response.status_code, 200)
        # Assert proper view is used
        self.assertEqual(response.resolver_match.func.view_class, ThingListView)

    def test_thing_list_view_accessible_by_name(self):
        """
        `ThingListView` should be accessible by `THING_LIST_VIEW_NAME`.
        """
        response = self.client.get(reverse(THING_LIST_VIEW_NAME))
        self.assertEqual(response.status_code, 200)

    def test_thing_list_view_uses_correct_template(self):
        """
        `ThingListView` should use template `THING_LIST_TEMPLATE`.
        """
        response = self.client.get(THING_LIST_URL)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, THING_LIST_TEMPLATE)

    def test_thing_list_view_displays_no_things(self):
        """
        `ThingListView` should display no `Thing` objects.
        """
        response = self.client.get(THING_LIST_URL)
        self.assertEqual(response.status_code, 200)
        # TODO: Add a message for when there are no `Thing` objects.
        # self.assertContains(response, 'No things are available.')
        self.assertQuerysetEqual(response.context['object_list'], [])

    def test_thing_list_view_displays_two_created_things(self):
        """
        `ThingListView` should display two created `Thing` objects.
        """
        # Create two `Thing` objects.
        thing1 = Thing.objects.create(name='Thing 1')
        thing2 = Thing.objects.create(name='Thing 2')
        number_of_things = 2
        # Get the response from `THING_LIST_URL`.
        response = self.client.get(THING_LIST_URL)
        # Check that the response is 200.
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, thing1.name, 2)
        self.assertContains(response, thing2.name, 2)

        # Would it be useful to check a specific attribute of `response` contains one of each `Thing` object?
        self.assertQuerysetEqual(
            response.context['object_list'],
            [thing1, thing2],
            ordered=False
        )

        # AssertionError: 2 != 1 : Found 2 instances of 'Thing 1' in response (expected 1)
        # self.assertContains(response, thing1.name, 1)

        # Check that the response contains the two `Thing` objects in each `object_list` and `thing_list`.
        self.assertEqual(
            len(response.context['object_list']),
            number_of_things
        )
        self.assertEqual(
            len(response.context['thing_list']),
            number_of_things
        )

        ################################################################
        ### Code created by GitHub Copilot. Not working as expected. ###
        # self.assertQuerysetEqual(
        #     response.context['object_list'],
        #     ['<Thing: Thing 1>', '<Thing: Thing 2>'],
        #     ordered=False
        # )
        ################################################################

    def test_queryset(self):
        """
        Test that the `ThingListView` `queryset` is correct.

        Is this test necessary? Are we testing our own code or Django's code?
        """
        # Create two `Thing` objects.
        thing1 = Thing.objects.create(name='Thing 1')
        thing2 = Thing.objects.create(name='Thing 2')
        number_of_things = 2
        # Get the `queryset` from the `ThingListView`.
        queryset = ThingListView().get_queryset()

        # ################################################################
        # ### Code created by GitHub Copilot. Not working as expected. ###
        # self.assertQuerysetEqual(
        #     queryset,
        #     ['<Thing: Thing 1>', '<Thing: Thing 2>'],
        #     ordered=False
        # )
        # ValueError: Negative indexing is not supported.
        # self.assertEqual(queryset[-1], thing2)
        # self.assertEqual(queryset[-2], thing1)

        # AssertionError: <QuerySet [<Thing: Thing 1>]> != [<Thing: Thing 1>]
        # self.assertEqual(queryset[0:1], [thing1])
        # AssertionError: <QuerySet [<Thing: Thing 1>, <Thing: Thing 2>]> != [<Thing: Thing 1>, <Thing: Thing 2>]
        # self.assertEqual(queryset[0:2], [thing1, thing2])

        # TypeError: 'Thing' object is not iterable
        # self.assertQuerysetEqual(queryset[0], thing1)
        # self.assertQuerysetEqual(queryset[1], thing2)
        # ################################################################

        ############################################################
        ### Colaboration with GitHub Copilot. Interesting results. #
        self.assertEqual(
            queryset.count(),
            number_of_things
            )
        self.assertEqual(
            queryset.first(),
            thing1
            )
        self.assertEqual(
            queryset.last(),
            thing2
            )
        self.assertQuerysetEqual(
            queryset[0:1],
            [thing1]
            )
        self.assertQuerysetEqual(
            queryset[0:2],
            [thing1, thing2],
            ordered=False
            )
        self.assertQuerysetEqual(
            queryset[1:2],
            [thing2]
            )
        self.assertQuerysetEqual(
            queryset[1:3],
            [thing2]
            )
        self.assertQuerysetEqual(
            queryset[2:3],
            []
            )
        ############################################################

