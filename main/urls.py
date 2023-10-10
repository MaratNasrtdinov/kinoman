from django.urls import path, re_path

from main.views import (FilmsView, NewsListView, RaitingView,
                        SearchResultsView, SerialsView, film_detail_view,
                        news_detail_view)

app_name = 'main'

urlpatterns = [
    path('films/', FilmsView.as_view(), name='films'),
    path('page/<int:page>/', FilmsView.as_view(), name='paginator'),
    path('serials/', SerialsView.as_view(), name='serials'),
    path('raiting/', RaitingView.as_view(), name='raiting'),
    path('category/', RaitingView.as_view(), name='category'),
    path('search/', SearchResultsView.as_view(), name='search_results'),
    path('search/', SearchResultsView.as_view(), name='search_results'),
    re_path(r'^show/(?P<film_id>[-\w]*)/$', film_detail_view, name='show'),
    path('news/', NewsListView.as_view(), name='news_list'),
    re_path(r'^news/(?P<news_id>[-\w]*)/$', news_detail_view, name='news'),
]
