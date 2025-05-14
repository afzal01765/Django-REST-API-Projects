from api.models import Book 
from api.serializers import SnippetSerializer
from rest_framework import generics


class BookListCreateAPIView(generics.ListCreateAPIView):   
    queryset = Book.objects.all()
    serializer_class = SnippetSerializer


class BookRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView): #update delete sigle element access korar jonno . 
    serializer_class = SnippetSerializer