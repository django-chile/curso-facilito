from django.conf.urls import url

from ..mascota.views import index

urlpatterns = [
    url(r'^$', index),
]