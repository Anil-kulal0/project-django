# from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import Noteserializer
from .models import Note      
# Create your views here.
@api_view(['GET'])
def getRoutes(request):
      routes = [
            { 
                  'Endpoint': '/notes/',
                  'method': 'GET',
                  'body': None,
                  'descriptions': 'Returns an arry of notes'
             },
            
            {
                  'Endpoint': '/notes/id',
                  'method': 'GET',
                  'body': None,
                  'descriptions': 'Returns a single note object'    
            },
            
            {
                  'Endpoint': '/notes/create/',
                  'method': 'POST',
                  'body': {'body':""},
                  'descriptions': 'Creates new notes with data sent in post req'
            },
            
            {
                  'Endpoint': '/notes/id/update/',
                  'method': 'PUT',
                  'body': {'body':""},
                  'descriptions': 'Creates an exiting note with data sent in'
            },
            
            {
                  'Endpoint': '/notes/id/delete/',
                  'method': 'DELETE',
                  'body': None,
                  'descriptions': 'Deletes an exiting note'
            }
            
      ]
      
      return Response(routes)


@api_view(['GET'])
def getnotes(request):
      notes = Note.objects.all()
      serializer = Noteserializer(notes, many= True )
      return Response(serializer.data)


@api_view(['GET'])
def getnote(request, pk):
      note = Note.objects.get(id=pk)
      serializer = Noteserializer(note, many=False )
      return Response(serializer.data)

@api_view(['POST'])
def creatnotes(request):
      data = request.data 
      
      note = Note.objects.create(
            body = data['body']
      )
      serializer = Noteserializer(note, many=False)
      return Response(serializer.data)



@api_view(['PUT'])
def updatenote(request, pk):
      data = request.data 
      
      note = Note.objects.get(id=pk)
          
      serializer = Noteserializer(note, data = request.data)
      if serializer.is_valid():
            serializer.save()
      return Response(serializer.data)
@api_view(['DELETE'])
def deletenote(request, pk):
      note = Note.objects.get(id=pk)
      note.delete()
      return Response('Note was deleted!')
      
      
