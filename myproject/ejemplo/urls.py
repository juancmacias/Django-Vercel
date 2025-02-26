from django.urls import path

from ejemplo.views import index


urlpatterns = [
    path('', index),
]