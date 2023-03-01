from django.urls import path

from things import views


app_name = 'things'
urlpatterns = [
    # URL route for the `ThingFormView` view, which will be used to create a new `Thing` object:
    path('form', views.ThingFormView.as_view(), name='form'),
    # URL route for the `ThingListView` view, which will be used to list all `Thing` objects:
    path('', views.ThingListView.as_view(), name='list'),
]