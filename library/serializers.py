# from rest_framework import serializers
# from .models import Author, Genre, Book

# class AuthorSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Author
#         fields = '__all__'

# class GenreSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Genre
#         fields = '__all__'

# class BookSerializer(serializers.ModelSerializer):
#     author = AuthorSerializer()
#     genre = GenreSerializer(many=True)

#     class Meta:
#         model = Book
#         fields = '__all__'

# library/serializers.py

from rest_framework import serializers
from .models import Author, Genre, Book

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'

class BookSerializer(serializers.ModelSerializer):
    author = serializers.PrimaryKeyRelatedField(queryset=Author.objects.all())
    genre = serializers.PrimaryKeyRelatedField(queryset=Genre.objects.all(), many=True)

    class Meta:
        model = Book
        fields = '__all__'

    def create(self, validated_data):
        genres = validated_data.pop('genre')  
        book = Book.objects.create(**validated_data)  
        book.genre.set(genres)  
        return book

    def update(self, instance, validated_data):
        genres = validated_data.pop('genre', None)  
        for attr, value in validated_data.items():
            setattr(instance, attr, value)  
        if genres is not None:
            instance.genre.set(genres)  
        instance.save()  
        return instance
