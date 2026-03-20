from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Item
from .serializers import ItemSerializer


@api_view(["GET"])
def items(request):
    items = Item.objects.all()
    serializer = ItemSerializer(items, many=True)
    return Response(serializer.data)


from django.shortcuts import render
# Create your views here.
def index(request):
    return render(request, 'index.html')
