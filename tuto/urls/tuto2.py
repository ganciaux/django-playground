from django.urls import path

from tuto import views

app_name = 'tuto2'
urlpatterns = [
    path('', views.index2, name='index'),
]