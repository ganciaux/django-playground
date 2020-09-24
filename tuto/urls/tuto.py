from django.urls import path

from tuto import views

app_name = 'tuto'
urlpatterns = [
    path('', views.index, name='index'),
]