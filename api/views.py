from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

from rest_framework import status 
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser

from api.models import Notes
from api.serializer import NoteSerializer


@api_view(['GET'])
@csrf_exempt
def loadAPIPage(request):
    notes = Notes.objects.all()
    serializer = NoteSerializer(notes, many=True)
    # return JsonResponse(serializer.data, safe=False)
    return Response(serializer.data)



@api_view(['POST'])
@csrf_exempt
def loadCreatePage(request):
    # data = JSONParser().parse(request)
    # print(data)
    serializer = NoteSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        # return JsonResponse(serializer.data, status=201)
        return Response(serializer.data, status=201)

    # return JsonResponse(serializer.errors, status=400)
    return Response(serializer.errors, status=400)
