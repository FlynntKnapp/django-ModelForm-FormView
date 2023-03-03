# `test_thing_views.py` Notes

```python
class ThingListViewTest(TestCase):
    #...
    def test_thing_list_view_displays_all_things(self):
        #...
        self.assertQuerysetEqual(
            response.context['object_list'],
            ['<Thing: Thing 1>', '<Thing: Thing 2>'],
            ordered=False
        )
```

```bash
Found 16 test(s).
Creating test database for alias 'default'...
System check identified no issues (0 silenced).
............F...
======================================================================
FAIL: test_thing_list_view_displays_all_things (things.tests.test_thing_views.ThingListViewTest.test_thing_list_view_displays_all_things)
Test that the `ThingListView` displays all `Thing` objects.
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:\Users\FlynntKnapp\Programming\django-ModelForm-FormView\things\tests\test_thing_views.py", line 59, in test_thing_list_view_displays_all_things
    self.assertQuerysetEqual(
  File "C:\Users\FlynntKnapp\.virtualenvs\django-ModelForm-FormView-XJWlRQLZ\Lib\site-packages\django\test\testcases.py", line 1317, in assertQuerysetEqual
    return self.assertDictEqual(Counter(items), Counter(values), msg=msg)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError: Counter({<Thing: Thing 1>: 1, <Thing: Thing 2>: 1}) != Counter({'<Thing: Thing 1>': 1, '<Thing: Thing 2>': 1})
- Counter({<Thing: Thing 1>: 1, <Thing: Thing 2>: 1})
+ Counter({'<Thing: Thing 1>': 1, '<Thing: Thing 2>': 1})
?          +                +     +                +


----------------------------------------------------------------------
Ran 16 tests in 0.073s

FAILED (failures=1)
Destroying test database for alias 'default'...
```
