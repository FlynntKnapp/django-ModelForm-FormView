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
        form.save()
        return super().form_valid(form)

    def get_success_url(self):
        # id_just_created = Thing.objects.latest('id').id
        # id_just_created = Thing.objects.last().id
        # id_just_created = Thing.objects.order_by('-id').first().id
        # id_just_created = Thing.objects.order_by('id').last().id
        the_thing_name = self.request.POST['name']
        id_just_created = Thing.objects.get(name=the_thing_name).id
        return reverse('things:detail', kwargs={'pk': id_just_created})

        # return '/things/'


class ThingDetailView(DetailView):
    model = Thing


class ThingListView(ListView):
    model = Thing

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['things'] = Thing.objects.all()
        return context
