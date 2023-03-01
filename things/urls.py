from django.urls import path

from things import views


app_name = 'things'
urlpatterns = [
    path('goodbuy', views.goodbuy, name='goodbuy'),

    path('form', views.ThingFormView.as_view(), name='form'),
    path('<int:pk>/', views.ThingDetailView.as_view(), name='detail'),
    path('', views.ThingListView.as_view(), name='list'),
]