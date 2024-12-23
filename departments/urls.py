from django.urls import path
from .views import (
    department_list, department_create, department_update, department_delete,
    product_list, product_create, product_update, product_delete,
    department_product_list
)

urlpatterns = [
    path('', department_list, name='department_list'),
    path('create/', department_create, name='department_create'),
    path('update/<int:pk>/', department_update, name='department_update'),
    path('delete/<int:pk>/', department_delete, name='department_delete'),

    path('<int:department_id>/products/', product_list, name='product_list'),
    path('<int:department_id>/products/create/', product_create, name='product_create'),
    path('<int:department_id>/products/update/<int:product_id>/', product_update, name='product_update'),
    path('<int:department_id>/products/delete/<int:product_id>/', product_delete, name='product_delete'), 

    path('products/', department_product_list, name='department_product_list'),
]