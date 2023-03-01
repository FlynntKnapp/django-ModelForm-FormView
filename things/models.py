from django.db import models
from django.urls import reverse

class Thing(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('things:detail', args=(self.pk))
        # return reverse('things:detail', kwargs={'pk': self.pk})
