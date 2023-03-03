from django.test import TestCase

from things.models import Thing


CLASS_WIDE_TEST_THING_NAME = 'Class-wide Test Thing Name'
TEST_THING_NAME_01 = 'Test Thing Name 01'
TEST_THING_NAME_02 = 'Test Thing Name 02'

THING_NAME_MAX_LENGTH = 100

THING_NAME_LABEL = 'Thing Name'


class ThingModelTest(TestCase):
    """
    Test suite for the `Thing` model.
    """

    @classmethod
    def setUpTestData(cls):
        """
        Set up non-modified objects used by all test methods.

        This specific function name `setUpTestData` is required by Django.
        """
        Thing.objects.create(name=CLASS_WIDE_TEST_THING_NAME)

    def test_thing_creation(self):
        """
        Test that a `Thing` object can be created.
        """
        thing = Thing.objects.create(name=TEST_THING_NAME_01)
        self.assertTrue(isinstance(thing, Thing))

    def test_thing_dunder_string_method(self):
        """
        Test that the `__str__` method returns the `Thing`'s `name`.
        """
        thing = Thing.objects.create(name=TEST_THING_NAME_01)
        self.assertEqual(thing.__str__(), thing.name)
        # The following is equivalent to the above:
        self.assertEqual(str(thing), thing.name)

    def test_name_max_length(self):
        """
        Test that the `name` field has a max length of 100 characters.
        """
        thing = Thing.objects.create(name=TEST_THING_NAME_01)
        max_length = thing._meta.get_field('name').max_length
        self.assertEqual(max_length, THING_NAME_MAX_LENGTH)

    def test_thing_name_label(self):
        """
        Test that the `name` field has the correct label.
        """
        thing = Thing.objects.create(name=TEST_THING_NAME_01)
        thing_name_field_label = thing._meta.get_field('name').verbose_name
        self.assertEqual(thing_name_field_label, THING_NAME_LABEL)

    def test_created_at_auto_now_add_is_true(self):
        """
        Test that the `created_at` field has option `auto_now_add=True`.
        """
        thing = Thing.objects.create(name=TEST_THING_NAME_01)
        self.assertTrue(thing._meta.get_field('created_at').auto_now_add)

    def test_updated_at_auto_now_is_true(self):
        """
        Test that the `updated_at` field has option `auto_now=True`.
        """
        thing = Thing.objects.create(name=TEST_THING_NAME_01)
        self.assertTrue(thing._meta.get_field('updated_at').auto_now)

    ##############################################################
    ### Are these tests necessary? Whose code is being tested? ###
    def test_created_date_not_none(self):
        """
        Test that the `created_at` field is automatically set to some
        value when the object is created.
        """
        thing = Thing.objects.create(name=TEST_THING_NAME_01)
        self.assertIsNotNone(thing.created_at)

    def test_updated_date_not_none(self):
        """
        Test that the `updated_at` field is automatically set to some
        value when the object is updated.
        """
        thing = Thing.objects.create(name=TEST_THING_NAME_01)
        # thing.name = TEST_THING_NAME_02 # Update the object
        # thing.save() # Save the object
        self.assertIsNotNone(thing.updated_at)

    def test_updated_at_not_equal_to_created_at(self):
        """
        Test that the `updated_at` field is not equal to the `created_at`
        field when the object is updated.
        """
        thing = Thing.objects.get(name=CLASS_WIDE_TEST_THING_NAME)
        thing.name = TEST_THING_NAME_02 # Update the object
        thing.save() # Save the object
        self.assertNotEqual(thing.updated_at, thing.created_at)

    def test_updated_at_greater_than_created_at(self):
        """
        Test that the `updated_at` field is greater than the `created_at`
        field when the object is updated.

        This test is probably not necessary, but it's here as an example of `assertGreater`.
        """
        thing = Thing.objects.get(name=CLASS_WIDE_TEST_THING_NAME)
        thing.name = TEST_THING_NAME_02
        thing.save()
        self.assertGreater(thing.updated_at, thing.created_at)
    ##############################################################
