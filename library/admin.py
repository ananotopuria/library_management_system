from django.contrib import admin
from .models import User, Author, Genre, Book

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'full_name', 'email', 'personal_number', 'birth_date')

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'email')
    search_fields = ('name', 'email')

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'published_date', 'stock')
    list_filter = ('genre', 'author', 'published_date')
    search_fields = ('title', 'author__name')
    filter_horizontal = ('genre',)