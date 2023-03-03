# Notes on What Errors Occur when Specific Lines of Code are Implemented or Disabled

## Modify Attributes of `ThingFormView` class in [`things/views.py`](../things/views.py)

### Disable `form_class = ThingForm`

1. HTTP `GET` request to the view URL

    * Error:

      ```bash
      TypeError: 'NoneType' object is not callable
      ```

### Disable `template_name = 'things/thing_form.html'`

1. HTTP `GET` request to the view URL

    * Error:

      ```bash
      django.core.exceptions.ImproperlyConfigured: TemplateResponseMixin requires either a definition of 'template_name' or an implementation of 'get_template_names()'
      ```

### Disable `success_url = reverse_lazy('things:thing_list')`

1. HTTP `GET` request to the view URL

    * Success

2. HTTP `POST` request to the view URL

    * Error:

      ```bash
      django.core.exceptions.ImproperlyConfigured: No URL to redirect to. Provide a success_url.
      ```

#### Solutions

```python
class ThingFormView(FormView):
    #...
    success_url = reverse_lazy('things:list')
```

```python
class ThingFormView(FormView):
    #...
    def get_success_url(self):
        #...
        return reverse('things:list')
```

```python
class ThingFormView(FormView):
  #...
    def get_success_url(self):
        #...
        return reverse_lazy('things:list')
```

### Disable our Implementation of `form_valid(self, form)`

1. HTTP `GET` request to the view URL

    * Success

2. HTTP `POST` request to the view URL
  
    * Functional Issue:
      * The `Thing` object is not created in the database.

### Implement `success_url = reverse('things:list')`

* Error:

  ```bash
  django.core.exceptions.ImproperlyConfigured: The included URLconf 'config.urls' does not appear to have any patterns in it. If you see the 'urlpatterns' variable with valid patterns in the file then the issue is probably caused by a circular import.
  ```

* Solution:

  ```python
  from django.urls import reverse_lazy

  class ThingFormView(FormView):
      #...
      success_url = reverse_lazy('things:list')
  ```
