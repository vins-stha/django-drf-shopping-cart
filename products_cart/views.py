
from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from django.shortcuts import render
from .models import Category,Product
from django.http import HttpResponse,HttpResponseBadRequest,request
from rest_framework.response import Response
from .serializers import *
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.parsers import FormParser, MultiPartParser
from django.http import Http404
from rest_framework import filters

from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets, mixins, status


# class based api view for category to create and view categories

class CategoryList(APIView):

    def get(self, request, format=None):
        cats = Category.objects.all()
        serializer_class = CategorySerializer(cats, many = True)

        return Response(serializer_class.data)


    def post(self,request,format=None):
        serializer = CategorySerializer(data=request.data)
        parser_classes = [MultiPartParser,FormParser]

        print(request.data)
        permission_classes = [IsAuthenticated]

        if not request.user.is_authenticated:
            return Response({'error':'Unauthorized. Please login as admin'}, status=401)

        if request.user.is_authenticated &  serializer.is_valid():

            serializer.save()
            print('DATA=', serializer.data)
            return Response(serializer.data,status = status.HTTP_201_CREATED)
        else:
            print('ERRORS=', serializer.errors)
            return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)


# class based api view for category to view individual category, delete and update categories

class CategoryDetail(APIView):
    def get_object(self,pk):
        try:
            return Category.objects.get(pk=pk)
        except Category.DoesNotExist:
            raise Http404

    def get(self,request,pk):
        cat = self.get_object(pk)
        serializer = CategorySerializer(cat)
        return Response(serializer.data)

    def put(self,request,pk, format=None):
        if not request.user.is_authenticated:
            return Response({'error': 'Unauthorized. Please login as admin'}, status=401)

        cat = self.get_object(pk)
        serializer = CategorySerializer(cat,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,pk,format=None):
        if not request.user.is_authenticated:
            return Response({'error': '401 Unauthorized. Please login as admin'}, status=401)

        category = self.get_object(pk)
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


## Product Views
class ProductViews(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [SearchFilter]
    search_fields = ['title', 'barcode']

from rest_framework import generics

class ProductList(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [SearchFilter]
    search_fields = ['title', 'barcode']

class ProductDetail(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_object(self, pk):
        try:
            return Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        cat = self.get_object(pk)
        serializer = ProductSerializer(cat)
        return Response(serializer.data)

from django.contrib.auth.models import User
class AdminViews(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = AdminSerializer



class CustomerViewSets(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
