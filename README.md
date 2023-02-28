# Django Basic Model Form Example

* Basic example of Django form usage.

## Application Structure

* Model:
  * `Thing`:
    * `name` (CharField)
    * `description` (TextField)
    * `created_at` (DateTimeField)
    * `updated_at` (DateTimeField)

* Views:
  * `ThingCreateView`:
    * `form_class` (ThingForm)
    * `template_name` (thing_create.html)
    * `success_url` (reverse_lazy('thing-list'))

  * `ThingListView`:
    * `template_name` (thing_list.html)
    * `queryset` (Thing.objects.all())
  
  * `ThingUpdateView`:
    * `form_class` (ThingForm)
    * `template_name` (thing_update.html)
    * `success_url` (reverse_lazy('thing-list'))
    * `queryset` (Thing.objects.all())

  * `ThingDeleteView`:
    * `template_name` (thing_delete.html)
    * `success_url` (reverse_lazy('thing-list'))
    * `queryset` (Thing.objects.all())

* URLs:
  * `thing-create` (ThingCreateView.as_view())
  * `thing-list` (ThingListView.as_view())
  * `thing-update` (ThingUpdateView.as_view())
  * `thing-delete` (ThingDeleteView.as_view())

## Resources

* <https://pypi.org/project/Django/>
* <https://pypi.org/project/docutils/>

* [Working with forms](https://docs.djangoproject.com/en/4.1/topics/forms/#working-with-forms)
* [`django.forms.Form`](https://docs.djangoproject.com/en/4.1/ref/forms/api/#django.forms.Form)
* [`django.forms.ModelForm`](https://docs.djangoproject.com/en/4.1/topics/forms/modelforms/#django.forms.ModelForm)
* [`user-admin-over-complicated-example/users/forms.py`](https://github.com/brucestull/examples/blob/main/django/user-admin-over-complicated-example/users/forms.py)
