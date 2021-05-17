from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
 
from bank.models import Bank
from bank.serializers import TutorialSerializer
from rest_framework.decorators import api_view


@api_view(['GET', 'POST', 'DELETE'])
def tutorial_list(request):
    if request.method == 'GET':
        tutorials = Bank.objects.all()
        title = request.GET.get('ifsc',None)
        if title is not None:
            tutorials = tutorials.filter(title__icontains=title)
        tutorials_serializer = TutorialSerializer(tutorials, many=True)
        return JsonResponse(tutorials_serializer.data,safe=False)
    elif request.method == 'POST':
        tutorial_data = JSONParser().parse(request)
        tutorials_serializer = TutorialSerializer(data=tutorial_data)
        if tutorials_serializer.is_valid():
            tutorials_serializer.save()
            return JsonResponse(tutorials_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(tutorials_serializer.data, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        count = Bank.objects.all().delete()
        return JsonResponse({'message': '{} Tutorials were deleted successfully!'.format(count[0])},status=status.HTTP_204_NO_CONTENT)
 
 
@api_view(['GET', 'PUT', 'DELETE'])
def tutorial_detail(request, branch, limit=None, offset=None):
    try: 
        tutorial = Bank.objects.filter(branch=branch)[limit:offset]
        if request.method == 'GET':
            tutorial_serializer = TutorialSerializer(tutorial,many=True)
            return JsonResponse(tutorial_serializer.data,safe=False)
        elif request.method == 'PUT':
            tutorial_data = JSONParser().parse(request)
            tutorial_serializer = TutorialSerializer(tutorial, data=tutorial_data)
            if tutorial_serializer.is_valid():
                tutorial_serializer.save()
                return JsonResponse(tutorial_serializer.data)
            return JsonResponse(tutorial_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        elif request.method == 'DELETE':
            tutorial.delete()
            return JsonResponse({'message':'Tutorial was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
    except Bank.DoesNotExist: 
        return JsonResponse({'message': 'The tutorial does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 
    # GET / PUT / DELETE tutorial
    
        
@api_view(['GET'])
def tutorial_list_published(request):
    tutorials = Bank.objects().filter(published=True)
    if request.method == 'GET':
        tutorial_serializer = TutorialSerializer(tutorials, many=True)
        return JsonResponse(tutorial_serializer.data, safe=False)