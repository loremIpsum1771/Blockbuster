from rest_framework.serializers import ModelSerializer

from .models import Movie,Genre


class MovieCreateSerializer(ModelSerializer):
    class Meta:
        model = Movie
        fields = [
            #'id',
            'title',
            'genre',
            'numberInStock',
            'dailyRentalRate',
            'publishDate',
            'liked'
        ]

class GenreSerializer(ModelSerializer):
    class Meta:
        model = Genre
        fields = [
            'id',
            'name'
        ]


class MovieSerializer(ModelSerializer):
    class Meta:
        model = Movie
        fields = [
            'id',
            'title',
            'genre',
            'numberInStock',
            'dailyRentalRate',
            'publishDate',
            'liked'
        ]
