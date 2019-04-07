from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    UpdateAPIView,
    DestroyAPIView,
    CreateAPIView
)
from rest_framework.mixins import DestroyModelMixin, UpdateModelMixin,CreateModelMixin
from .models import Movie, Genre
from rest_framework import permissions
from .serializers import (MovieSerializer,GenreSerializer,MovieCreateSerializer)

#ListView
class GenreListAPIView(ListAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer

class MovieListAPIView(ListAPIView):
    queryset = Movie.objects.all()
    serializer_class =  MovieSerializer

#Retrieve API
class MovieDetailAPIView(RetrieveAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class GenreDetailAPIView(RetrieveAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer

#Destroy API
class MovieDestroyAPIView(DestroyModelMixin,RetrieveAPIView):#DestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    #permission_classes = (permissions.IsAuthenticated,)    
    def delete(self,request,*args,**kwargs):
        return self.destroy(request,*args,**kwargs)

#Update API

class MovieUpdateAPIView(DestroyModelMixin, UpdateModelMixin, RetrieveAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = (permissions.IsAuthenticated,)
    def put(self,request,*args, **kwargs):
        return self.update(request,*args,**kwargs)
    def post(self,request,*args, **kwargs):
        return self.update(request,*args,**kwargs)

    def patch(self,request,*args, **kwargs):
        return self.update(request,*args,**kwargs)
    

#Create APIView

class MovieCreateAPIView(CreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    #permission_classes = (permissions.IsAuthenticated,)