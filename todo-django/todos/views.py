from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Todo
from .serializers import TodoSerializers
# Create your views here.

@api_view(['GET'])
def todo_index_create(index):
    todos = Todo.objects.all()
    serializer = TodoSerializers(todos, many=True)
    return Response(serializer.data)