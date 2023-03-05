# Django Basic Model Form Example

* Basic example of Django `ModelForm` usage.

## `things` Application Structure

* Models:
  * `Thing`
    | Field | Type | Description |
    | --- | --- | --- |
    | `name` | `CharField` | Name of the thing. |
    | `created_at` | `DateTimeField` | Date and time the thing was created. |
    | `updated_at` | `DateTimeField` | Date and time the thing was last updated. |

* Views:
  * `ThingCreateView`
    | Attribute | Value |
    | --- | --- |
    | `form_class` | `ThingForm` |
    | `template_name` | `thing_create.html` |
    | `success_url` | `reverse_lazy('thing-list')` |

  * `ThingListView`
    | Attribute | Value |
    | --- | --- |
    | `template_name` | `thing_list.html` |
    | `queryset` | `Thing.objects.all()` |
  
  * `ThingDetailView`
    | Attribute | Value |
    | --- | --- |
    | `template_name` | `thing_detail.html` |
    | `queryset` | `Thing.objects.all()` |

  * `ThingUpdateView`
    | Attribute | Value |
    | --- | --- |
    | `form_class` | `ThingForm` |
    | `template_name` | `thing_update.html` |
    | `success_url` | `reverse_lazy('thing-list')` |
    | `queryset` | `Thing.objects.all()` |

  * `ThingDeleteView`
    | Attribute | Value |
    | --- | --- |
    | `template_name` | `thing_delete.html` |
    | `success_url` | `reverse_lazy('thing-list')` |
    | `queryset` | `Thing.objects.all()` |

* URLs:

  | URL Route | View | View Name |
  | --- | --- | --- |
  | `things/create/` | `ThingCreateView.as_view()` | `create` |
  | `things/list/` | `ThingListView.as_view()` | `list` |
  | `things/<int:pk>/` | `ThingDetailView.as_view()` | `detail` |
  | `things/<int:pk>/update/` | `ThingUpdateView.as_view()` | `update` |
  | `things/<int:pk>/delete/` | `ThingDeleteView.as_view()` | `delete` |

## Interesting and/or New Concepts

* In a `FormView`, does `form_valid()` execute before `get_success_url()`?
  * Yes.
    * Confirmed via breakpoints in `form_valid()` and `get_success_url()`.
    * Confirm via Django documentation for [`FormView`](https://docs.djangoproject.com/en/4.1/ref/class-based-views/generic-editing/#django.views.generic.edit.FormView) or `FormView` parent classes.

## Example Code

### `ThingFormView`

* `ThingFormView` in [`things/views.py`](./things/views.py):
  * We create the object directly rathen than use `form.save()` because we want to use the `id` of the newly created `Thing` object in `get_success_url()`.

  ```python
  class ThingFormView(FormView):
      form_class = ThingForm
      template_name = 'things/thing_form.html'

      def form_valid(self, form):
          # Create a `thing` attribute of `self`: `self.thing`
          # This will allow us to access the `id` of the newly created `Thing` object in `get_success_url()`.
          self.thing = Thing.objects.create(name=form.cleaned_data['name'])
          return super(ThingFormView, self).form_valid(form)

      def get_success_url(self):
          # We can get the `id` of the newly created `Thing` object from `self.thing.id` and use that to build the URL.
          return reverse('things:detail', kwargs={'pk': self.thing.id})
  ```

### `return_hard_coded_httpresponse()`

* Strings which contain HTML will render as HTML in the browser.

```python
def return_hard_coded_httpresponse(request):
    return HttpResponse(
        '<a href="/admin/"><code>admin:index</code></a>'
        '<br>'
        '<a href="/things/"><code>things:list</code></a>'
        '<h1><code>things:goodbuy</code></h1>'
        '<div>Goodbuy, world! Enjoy the Sails!</div>'
    )
```

## Resources

* <https://pypi.org/project/Django/>
* <https://pypi.org/project/docutils/>
* <https://pypi.org/project/coverage/>
* <https://pypi.org/project/django-nose/>

* [Working with forms](https://docs.djangoproject.com/en/4.1/topics/forms/#working-with-forms)
* [`django.views.generic.edit.FormView`](https://docs.djangoproject.com/en/4.1/ref/class-based-views/generic-editing/#django.views.generic.edit.FormView)
* [`django.forms.Form`](https://docs.djangoproject.com/en/4.1/ref/forms/api/#django.forms.Form)
* [`django.forms.ModelForm`](https://docs.djangoproject.com/en/4.1/topics/forms/modelforms/#django.forms.ModelForm)
* [`user-admin-over-complicated-example/users/forms.py`](https://github.com/brucestull/examples/blob/main/django/user-admin-over-complicated-example/users/forms.py)
* [`django.forms.models` - github.com/django](https://github.com/django/django/blob/main/django/forms/models.py)
* [Measuring Coverage - django-testing-docs.readthedocs.io](https://django-testing-docs.readthedocs.io/en/latest/coverage.html)
