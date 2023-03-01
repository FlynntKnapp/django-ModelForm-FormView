from django.urls import reverse_lazy
from django.views.generic import ListView, FormView

from things.models import Thing
from things.forms import ThingForm


class ThingFormView(FormView):
    form_class = ThingForm
    template_name = 'things/thing_form.html'
    success_url = reverse_lazy('things:list')
    # Creates an error if you use `reverse()` instead of `reverse_lazy()`:
    # success_url = reverse('things:list')

    def form_valid(self, form):
        """
        Actions to perform is the form is valid:
        - Use the `save()` method of the `form` to create a new `Thing`
        object from the data input into the form.
        - Use the parent class's `form_valid()` method to redirect to
        the `success_url`, defined above.
        """
        form.save()
        return super(ThingFormView, self).form_valid(form)


class ThingListView(ListView):
    model = Thing
