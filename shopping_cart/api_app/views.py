from django.shortcuts import render, get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import CartItem
from .serializers import CartItemSerializer


class CartItemsViews(APIView):
    def post(self, request):
        serializer = CartItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


    def get(self, request):
        items = CartItem.objects.all()
        serializer = CartItemSerializer(items, many=True)
        return Response({"data": serializer.data}, status=status.HTTP_200_OK)


class CartItemViews(APIView):
    def get(self, request, id):
        item = get_object_or_404(CartItem, id=id)
        serializer = CartItemSerializer(item)
        return Response({"data": serializer.data}, status=status.HTTP_200_OK)


    def patch(self, request, id):
        item = get_object_or_404(CartItem, id=id)
        serializer = CartItemSerializer(item, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, id):
        item = get_object_or_404(CartItem, id=id)
        item.delete()
        return Response({"data": None}, status=status.HTTP_200_OK)
