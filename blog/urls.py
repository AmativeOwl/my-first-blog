from django.urls import path
from . import views

urlpatterns = [
    # url pattern
    path('', views.post_list, name='post_list'),
]