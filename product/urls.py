from django.urls import path
from product.views import ProdustListView, AddProductView , DeleteProductView, UpdateProductView

urlpatterns = [
    path('list', ProdustListView.as_view()),
    path('new', AddProductView.as_view()),
    path('delete/<int:pk>', DeleteProductView.as_view()),
    path('update/<int:pk>',UpdateProductView.as_view()),
]
