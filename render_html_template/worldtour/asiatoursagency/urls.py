from django.urls import path
from . import views  # Make sure this import is correct

urlpatterns = [
    path('', views.index, name='index'),  # This should point to your index view
]