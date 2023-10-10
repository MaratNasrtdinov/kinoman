from django.db import models

from users.models import User


class Category(models.Model):
    name = models.CharField(max_length=64, unique=True, primary_key=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'




class Genre(models.Model):
    name = models.CharField(max_length=64, unique=True, primary_key=True)

    def __str__(self):
        return self.name

class Film(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=128, unique=False, primary_key=False)
    desc = models.TextField(max_length=320)
    genre = models.ForeignKey(to=Genre, on_delete=models.SET_DEFAULT, default='Боевик')
    video = models.CharField(max_length=256, default='Пусто')
    image = models.ImageField(upload_to='main_images')
    category = models.ForeignKey(to=Category, on_delete=models.SET_DEFAULT, default='Фильмы')
    raiting = models.FloatField(default=0)
    year = models.IntegerField(default=0)
    director = models.CharField(max_length=128, default='Пусто')

    def __str__(self):
        return f'{self.name} | {self.category.name}'

class CommentModel(models.Model):
    film = models.ForeignKey(to=Film, related_name='comments', on_delete=models.CASCADE)
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return 'Комментарий от {} для {}'.format(self.user, self.film)

class News(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32)
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

