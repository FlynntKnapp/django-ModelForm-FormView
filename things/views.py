from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import ListView, DetailView, FormView, CreateView

from things.models import Thing
from things.forms import ThingForm


def goodbuy(request):
    return HttpResponse(
        '<a href="/admin/"><code>admin:index</code></a>'
        '<br>'
        '<a href="/things/"><code>things:list</code></a>'
        '<h1><code>things:goodbuy</code></h1>'
        '<div>Goodbuy, world! Enjoy the Sails!</div>'
    )


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


class ThingDetailView(DetailView):
    model = Thing


class ThingListView(ListView):
    model = Thing

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['things'] = Thing.objects.all()
        return context
