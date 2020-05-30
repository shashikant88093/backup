from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from django.contrib.auth.models import User
from .models import Movie, Rating
from .serializers import MovieSerializer, RatingSerializer
from rest_framework.authentication import TokenAuthentication

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = RatingSerializer
    authentication_classes = (TokenAuthentication,)


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    authentication_classes = (TokenAuthentication,)

    @action(detail=True,methods=['POST'])
    def rate_movie(self,requset,pk=None):
        if 'stars' in requset.data:
            movie = Movie.objects.get(id=pk)
            stars = requset.data['stars']
            user = requset.user
            # user = User.objects.get(id=1)
            # print('movie stars user',user.username)
            try:
                rating = Rating.objects.get(user=user.id,movie=movie.id)
                rating.stars = stars
                rating.save()
                serializer = RatingSerializer(rating,many=False)
                response = {'message':'its working'}
                return Response(response, status=status.HTTP_200_OK )
            except:
                rating = Rating.objects.create(user=user, movie=movie, stars=stars)
                serializer = RatingSerializer(rating,many=False)
                response = {'message': 'Rating created','result':serializer.data}
                return Response(response, status=status.HTTP_200_OK)

        else:
            response = {'message': 'you need to provide stars'}
            return Response(response, status=status.HTTP_404_NOT_FOUND)


class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
    authentication_classes = (TokenAuthentication,)

