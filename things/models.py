from django.db import models
from django.urls import reverse

class Thing(models.Model):
    """
    Model for a `Thing` object.

    This is a simple object with only three fields:
    - `name`: a `CharField` with a max length of 100 characters.
    - `created_at`: a `DateTimeField` that is automatically set to the current date/time when the object is created.
    - `updated_at`: a `DateTimeField` that is automatically set to the current date/time when method `Model.save()` is executed.
    """
    name = models.CharField(
        max_length=100,
        verbose_name='Thing Name',
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
