from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from .models import Category, Product, Brand
from .serializers import CategorySerializer, BrandSerializer, ProductSerializer


# Create your views here.


class CategoryViewSet(viewsets.ViewSet):
    """
    A simple ViewSet for viewing the categories.
    """
    queryset = Category.objects.all()

    def list(self, request):
        serializer = CategorySerializer(self.queryset, many=True)
        return Response(serializer.data)
