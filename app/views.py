from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .serializers import ResumeSerializer
from .models import *

@api_view(["GET", "POST", "DELETE"])
def resumeView(request, pk=None):

    if request.method == "GET":

        if pk is not None:
            
            try:
                resume = ResumeModel.objects.get(id=pk)
                serializer = ResumeSerializer(resume)
                return Response(serializer.data , status=status.HTTP_200_OK)
            
            except ResumeModel.DoesNotExist:
                return Response({"error":"Resume Id not found"}, status=status.HTTP_404_NOT_FOUND)

        resumes = ResumeModel.objects.all()
        serializer = ResumeSerializer(resumes, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

    if request.method == "POST":
        serializer = ResumeSerializer(data = request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    "message": "Resume Created Successfully!",
                    "data": serializer.data
                },
                status= status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)


    if request.method == "DELETE":

        if pk is None:
            return Response({"error": "Id is required for deletion"}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            resumes = ResumeModel.objects.get(id=pk)
            resumes.delete()
            return Response({"message" : "Deletion Successful!"}, status=status.HTTP_204_NO_CONTENT)
        except ResumeModel.DoesNotExist:
            return Response({"error": "Resume Id not found"}, status=status.HTTP_404_NOT_FOUND)
    

@api_view(["GET"])
def health_check(request):
    return Response({"status": "ok"}, status=status.HTTP_200_OK)