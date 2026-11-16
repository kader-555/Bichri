from django.shortcuts import render

from .serializers import RatingSerializer, UserSerializer
from ..models import Rating, User 
from rest_framework.views import APIView
from rest_framework.response import Response


class UserListAV(APIView):
    def get(self,request):
        users = User.objects.all()
        serializer = UserSerializer(users, many= True)
        return Response(serializer.data)

class RatingListAV(APIView):
    
    def get(self, request):
        ratings = Rating.objects.all()
        serializer = RatingSerializer(ratings,many=True)
        return Response(serializer.data)

class ListUserByRatingAV(APIView):
    def get(self, request, rating):
        if rating < 1 or rating > 5:
            return Response({"error": "Rating must be between 1 and 5."}, status=400)
        if Rating.DoesNotExist:
            return Response({"error": "No ratings found."}, status=404)
        users = User.objects.filter(ratings_received__score=rating).distinct()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)