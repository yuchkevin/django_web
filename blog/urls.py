from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),  # /blog/ 访问 post_list
]
