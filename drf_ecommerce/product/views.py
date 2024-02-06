from drf_spectacular.utils import extend_schema
from rest_framework import viewsets
from rest_framework.response import Response

from drf_ecommerce.product.models import Category, Brand, Product
from drf_ecommerce.product.serializers import CategorySerializer, BrandSerializer, ProductSerializer


class CategoryViewSet(viewsets.ViewSet):
    """
    A simple ViewSet for viewing and editing categories.
    """
    queryset = Category.objects.all()

    @extend_schema(responses={200: CategorySerializer(many=True)}, tags=["Category"])
    def list(self, request):
        serializer = CategorySerializer(self.queryset, many=True)
        return Response(serializer.data)


class BrandViewSet(viewsets.ViewSet):
    """
    A simple ViewSet for viewing and editing brands.
    """
    queryset = Brand.objects.all()

    @extend_schema(responses={200: BrandSerializer(many=True)}, tags=["Brand"])
    def list(self, request):
        serializer = BrandSerializer(self.queryset, many=True)
        return Response(serializer.data)


class ProductViewSet(viewsets.ViewSet):
    """
    A simple ViewSet for viewing and editing products.
    """
    queryset = Product.objects.all()

    @extend_schema(responses={200: ProductSerializer(many=True)}, tags=["Product"])
    def list(self, request):
        serializer = ProductSerializer(self.queryset, many=True)
        return Response(serializer.data)
