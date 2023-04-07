from .views import *
from django.urls import path

urlpatterns = [
    path('courses', courseListView),
    path('courses/<int:pk>', courseDetailView),
]
