from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('jobs', views.port_list, name='port_list'),
    path('jobs/<int:job_id>', views.port_detail, name='port_detail'),
]