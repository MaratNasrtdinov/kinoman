from django.contrib import admin

from main.models import Category, CommentModel, Film, Genre, News

admin.site.register(Category)

@admin.register(Film)
class FilmAdmin(admin.ModelAdmin):
    list_display = ('name', 'category')
    fields = ('id', ('name', 'desc'), ('raiting', 'year'), 'image', 'video', 'genre', 'director', 'category')
    search_fields = ('name',)
    ordering = ('name',)
    readonly_fields = ('id',)

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('name',)
    fields = ('name',)

@admin.register(CommentModel)
class CommentAdmin(admin.ModelAdmin):
    fields = ('film', 'user', 'text', 'created')
    readonly_fields = ('film', 'user', 'created')

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('name', 'created')
    fields = ('id', 'name', 'text', 'created')
    search_fields = ('name',)
    ordering = ('id',)
    readonly_fields = ('id', 'created')
