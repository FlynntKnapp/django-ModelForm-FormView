from django.urls import reverse_lazy
from django.urls import reverse
from django.views.generic import ListView, FormView

from things.models import Thing
from things.forms import ThingForm


class ThingFormView(FormView):
    """
    View for a user to create a new `Thing`.

    This view inherits the `FormView` class from Django's generic views.

    This view has the following attributes:
    - `form_class`: the form class to use to create the form.
    - `template_name`: the template to use to render the form.
    - `success_url`: the URL to redirect to if the form is valid.
    - `form_valid()`: the method to execute if the form is valid.
    """
    form_class = ThingForm
    template_name = 'things/thing_form.html'
    success_url = reverse_lazy('things:list')


    def form_valid(self, form):
        """
        Actions to perform is the form is valid:
        - Use the `save()` method of the `form` to create a new `Thing`
        object from the data input into the form.
        - Use the parent class's `form_valid()` method to redirect to
        the `success_url`, defined above.

        This method is required for the `Thing` object to be created.

        We are using the `save()` method of `django.forms.models.BaseModelForm`.
        """
        form.save()
        return super(ThingFormView, self).form_valid(form)


class ThingListView(ListView):
    model = Thing
