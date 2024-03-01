from django.urls import path
from . import views
urlpatterns = [
    path('/product' , views.getProducts ,name='product'),
    path('/add/' , views.addProducts ,name='addProducts'),
    # path('add/', AddProductView.as_view(), name='addProducts'),
    path('/registration/' , views.registration ,name='registration'),
    path('/delete/<int:id>/' , views.delProducts ,name='delProducts'),
    path('/update/<int:id>/' , views.updateProducts ,name='updateProducts'),
    # path('update/<int:pk>/', UpdateProductView.as_view(), name='updateProducts'),

    
]
