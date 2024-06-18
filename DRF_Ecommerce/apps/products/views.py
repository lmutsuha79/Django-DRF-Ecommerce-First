from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from .models import Category, Product, Brand
from .serializers import CategorySerializer, BrandSerializer, ProductSerializer
from drf_spectacular.utils import extend_schema


# Create your views here.


class CategoryViewSet(viewsets.ViewSet):
    """
    A simple ViewSet for viewing the categories.
    """
    queryset = Category.objects.all()

    @extend_schema(responses=CategorySerializer)
    def list(self, request):
        serializer = CategorySerializer(self.queryset, many=True)
        return Response(serializer.data)
