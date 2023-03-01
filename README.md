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

## Resources

* <https://pypi.org/project/Django/>
* <https://pypi.org/project/docutils/>

* [Working with forms](https://docs.djangoproject.com/en/4.1/topics/forms/#working-with-forms)
* [`django.forms.Form`](https://docs.djangoproject.com/en/4.1/ref/forms/api/#django.forms.Form)
* [`django.forms.ModelForm`](https://docs.djangoproject.com/en/4.1/topics/forms/modelforms/#django.forms.ModelForm)
* [`user-admin-over-complicated-example/users/forms.py`](https://github.com/brucestull/examples/blob/main/django/user-admin-over-complicated-example/users/forms.py)
