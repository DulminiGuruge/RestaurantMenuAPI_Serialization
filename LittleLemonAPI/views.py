from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import MenuItem
from .serializers import MenuItemSerializer
from django.shortcuts import get_object_or_404


# Create your views here.
@api_view()
def menu_items(request):
    if request.method == 'GET':
        items = MenuItem.objects.select_related('category').all()
        serialized_item = MenuItemSerializer(items, many=True)
        return Response(serialized_item.data)

    if request.method == 'POST':
        serialized_item = MenuItemSerializer(data = request.data)
        serialized_item.is_valid(raise_exception=True)
        serialized_item.save()
        return Response(serialized_item.data, status.HTTP_201_CREATED)


@api_view()
def single_item(request, id):
    item = get_object_or_404(MenuItem, pk = id)
    serialized_item = MenuItemSerializer(item)
    return Response(serialized_item.data)

