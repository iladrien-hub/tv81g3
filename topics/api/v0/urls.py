from django.urls import path

from topics.api.v0.views import ping, ListTopics

app_name = 'topics'

urlpatterns = [
    path('', ping, name='ping'),

    path('topics/', ListTopics.as_view(), name="topics")
]