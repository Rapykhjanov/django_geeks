from django.contrib import admin
from .models import Director, Movie, Review

@admin.register(Director)
class DirectorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'director', 'duration')
    list_filter = ('director',)
    search_fields = ('title', 'description')

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'movie', 'stars', 'text')
    list_filter = ('stars',)
    search_fields = ('movie__title', 'text')
