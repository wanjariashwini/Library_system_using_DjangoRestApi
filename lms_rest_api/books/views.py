from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from books.models import Books
from rest_framework.decorators import api_view
from books.serializers import BooksSerializer


@api_view(['GET'])
def hc(request):
    message = {'message': 'Server is running fine'}
    return JsonResponse(message)


@api_view(['POST'])
def addBook(request):
    book_data = JSONParser().parse(request)
    book_serializer = BooksSerializer(data=book_data)
    if book_serializer.is_valid():
        book_serializer.save()
        return JsonResponse(book_serializer.data, status=status.HTTP_201_CREATED)
    return JsonResponse(book_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def getAllBooks(request):
    book_data = Books.objects.all()
    book_serializer = BooksSerializer(book_data, many=True)
    return JsonResponse(book_serializer.data, safe=False)


@api_view(['GET'])
def getBook(request, id):
    # emp_id = request.query_params.get(id)
    book_data = Books.objects.filter(id=id)
    print(book_data)
    book_serializer = BooksSerializer(book_data, many=True)
    return JsonResponse(book_serializer.data, safe=False)


@api_view(['PUT'])
def updateBook(request, id):
    book_data1 = Books.objects.get(id=id)
    book_data = JSONParser().parse(request)
    book_serializer = BooksSerializer(book_data1, data=book_data)
    if book_serializer.is_valid():
        book_serializer.save()
        return JsonResponse(book_serializer.data)
    return JsonResponse(book_serializer.errors, status=status.HTTP_400_BAD_R)


@api_view(['DELETE'])
def deleteBook(request, id):
    book_data = Books.objects.get(id=id)
    book_data.delete()
    return JsonResponse({'message': 'Book deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
