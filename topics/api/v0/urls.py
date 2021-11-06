from django.urls import path

from topics.api.v0.views import ping

app_name = 'topics'

urlpatterns = [
    path('', ping, name='ping'),
]