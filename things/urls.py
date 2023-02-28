from django.urls import path

from things import views


app_name = 'things'
urlpatterns = [
    path('goodbuy', views.goodbuy, name='goodbuy'),

    path('', views.ThingListView.as_view(), name='list'),
]