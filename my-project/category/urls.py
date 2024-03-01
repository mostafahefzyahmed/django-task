from django.urls import path
from . import views

urlpatterns = [
    path('' , views.addCategory , name='addCategory'),
    path('/list/' , views.getCategory , name='getCategory'),
]
