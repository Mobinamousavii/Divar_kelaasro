from product.models import Product
from django.http.response import HttpResponse
from rest_framework.generics import ListAPIView
from product.serializers import ProductSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters


class ProdustListView(ListAPIView):
        queryset = Product.objects.all()
        serializer_class = ProductSerializer
        filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
        filterset_fields = {
                'urgent' :['exact'],
                'has_photo' : ['exact'],
                'price' : ['exact', 'gte', 'lte'],
                'city' : ['exact', 'icontains']
        }
        search_fields = ['title', 'city']
        ordering_fields = ['date_time']
        


