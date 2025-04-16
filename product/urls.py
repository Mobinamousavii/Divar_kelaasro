from django.urls import path
from product.views import ProdustListView

urlpatterns = [
    path('list', ProdustListView.as_view()),
]
