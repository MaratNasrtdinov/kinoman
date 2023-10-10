from itertools import islice

from main.models import Film, News


def sidebar_films(request):
    films = Film.objects.filter(category='Фильмы')
    sidebar_films = list(islice(films, 4))
    return {'sidebar_films': sidebar_films}

def sidebar_news(request):
    news = News.objects.order_by('-id')
    sidebar_news = list(islice(news, 2))
    return {'sidebar_news': sidebar_news}