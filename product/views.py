from product.models import Product
from django.http.response import HttpResponse
from rest_framework.generics import ListAPIView, CreateAPIView, DestroyAPIView, UpdateAPIView
from product.serializers import ProductSerializer, ProductListSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.permissions import IsAuthenticated , IsAdminUser
from product.permisions import IsCreatorOrAdmin
class ProdustListView(ListAPIView):
        queryset = Product.objects.all()
        serializer_class = ProductListSerializer
        filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
        filterset_fields = {
                'urgent' :['exact'],
                'has_photo' : ['exact'],
                'price' : ['exact', 'gte', 'lte'],
                'city' : ['exact', 'icontains']
        }
        search_fields = ['title', 'city']
        ordering_fields = ['date_time']
class RealEstateListView(ListAPIView):
    queryset = Product.objects.filter(type=Product.ProductType.REAL_ESTATE)
    serializer_class = ProductSerializer
class VehiclesListView(ListAPIView):
    queryset = Product.objects.filter(type=Product.ProductType.VEHICLES)
    serializer_class = ProductSerializer

class AddProductView(CreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_create(self, serializer):
        serializer.save(user = self.request.user)
class DeleteProductView(DestroyAPIView):
     permission_classes = [IsAuthenticated, IsCreatorOrAdmin]
     queryset = Product.objects.all()
     serializer_class = ProductSerializer
class UpdateProductView(UpdateAPIView):
     permission_classes = [IsAuthenticated]
     queryset = Product.objects.all()
     serializer_class = ProductSerializer