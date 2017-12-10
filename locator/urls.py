from django.urls import path

from . import views

app_name = 'locator'
urlpatterns = [
    path('', views.index, name='index'),
    path('update_location/', views.update_location, name='update_location'),
]
