from django.shortcuts import render
from .models import student
from .serializers import studentSerializer
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets

# Create your views here.


# Serialziation JsonResponse

# def home(request):
    # if request.method == 'GET':
    #     snippets = student.objects.all()
    #     serializer = studentSerializer(snippets, many=True)
    #     return JsonResponse(serializer.data, safe=False)

    # elif request.method == 'POST':
    #     data = JSONParser().parse(request)
    #     serializer = studentSerializer(data=data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return JsonResponse(serializer.data, status=201)
    #     return JsonResponse(serializer.errors, status=400)

# @csrf_exempt
# def student_detail(request, pk):
    # """
    # Retrieve, update or delete a code snippet.
    # """
    # try:
    #     snippet = student.objects.get(pk=pk)
    # except student.DoesNotExist:
    #     return HttpResponse(status=404)

    # if request.method == 'GET':
    #     serializer = studentSerializer(snippet)
    #     return JsonResponse(serializer.data)

    # elif request.method == 'PUT':
    #     data = JSONParser().parse(request)
    #     serializer = studentSerializer(snippet, data=data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return JsonResponse(serializer.data)
    #     return JsonResponse(serializer.errors, status=400)

    # elif request.method == 'DELETE':
    #     snippet.delete()
    #     return HttpResponse(status=204)


# Serialzation Response and Request

# @api_view(['GET', 'POST'])
# def home(request):
        
#     """
#     List all code snippets, or create a new snippet.
#     """
#     if request.method == 'GET':
#         students = student.objects.all()  # Updated model name
#         serializer = studentSerializer(students, many=True)  # Updated serializer
#         return Response(serializer.data)

#     elif request.method == 'POST':
#         serializer = studentSerializer(data=request.data)  # Updated serializer
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
# @api_view(['GET', 'PUT', 'DELETE'])
# def student_detail(request, pk):
   
#     """
#     Retrieve, update or delete a code snippet.
#     """
#     try:
#         data = student.objects.get(pk=pk)  # Updated model name
#     except student.DoesNotExist:  # Updated model name
#         return Response(status=status.HTTP_404_NOT_FOUND)

#     if request.method == 'GET':
#         serializer = studentSerializer(data)  # Updated serializer
#         return Response(serializer.data)

#     elif request.method == 'PUT':
#         serializer = studentSerializer(data, data=request.data)  # Updated serializer
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     elif request.method == 'DELETE':
#         data.delete()  # Updated model name
#         return Response(status=status.HTTP_204_NO_CONTENT)


class StudentViewSet(viewsets.ModelViewSet):
    queryset= student.objects.all()
    serializer_class = studentSerializer