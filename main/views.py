from django.db.models import Q
from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView

from common.views import TitleMixin
from main.forms import CommentForm
from main.models import Film, News
from users.models import User


class BaseView(TemplateView):
    template_name = 'main/base.html'

    def get_context_data(self, **kwargs):
        context = super(BaseView, self).get_context_data()
        context['films'] = Film.objects.filter(category="Фильмы")
        return context

class IndexView(TitleMixin, TemplateView):
    template_name = 'main/index.html'
    title = 'КиноМан'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data()
        context["serials"] = Film.objects.filter(category="Сериалы").order_by("-id")
        context['films'] = Film.objects.filter(category="Фильмы").order_by("-id")
        return context

class FilmsView(TitleMixin, ListView):
    model = Film
    template_name = 'main/films.html'
    title = 'КиноМан | Фильмы'

    def get_queryset(self):
        queryset = super(FilmsView, self).get_queryset()
        return queryset

    def get_context_data(self, **kwargs):
        context = super(FilmsView, self).get_context_data()
        context['films'] = Film.objects.filter(category="Фильмы")
        return context

class SerialsView(TitleMixin, ListView):
    model = Film
    template_name = 'main/serials.html'
    title = 'КиноМан | Сериалы'

    def get_queryset(self):
        queryset = super(SerialsView, self).get_queryset()
        return queryset

    def get_context_data(self, **kwargs):
        context = super(SerialsView, self).get_context_data()
        context['serials'] = Film.objects.filter(category="Сериалы")
        return context

class RaitingView(TitleMixin, ListView):
    model = Film
    title = 'Киноман | Рейтинг'
    template_name = 'main/raiting.html'

    def get_context_data(self, **kwargs):
        context = super(RaitingView, self).get_context_data()
        context['films'] = Film.objects.order_by('-raiting')
        return context


def film_detail_view(request, film_id):
    film = Film.objects.get(id=film_id)
    try:
        user = User.objects.get(id=request.user.id)
    except Exception:
        user = 'k'
    # Комментарии
    comments = film.comments.filter(film=film)

    if request.method == 'POST':
        comment_form = CommentForm(data={'user': user, 'text': request.POST['text']})
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.film = film
            new_comment.user = user
            new_comment.save()

    else:
        comment_form = CommentForm()
    print(comment_form.errors)
    print(request.user)

    return render(request, 'main/show.html',
                  context={
                      'user': user,
                      'film': film,
                      'comments': comments,
                      'comment_form': comment_form,
                  })



class SearchResultsView(ListView):
    model = Film
    template_name = 'main/search_results.html'

    def get_queryset(self):
        query = self.request.GET.get('search_field')
        object_list = Film.objects.filter(
            Q(name__icontains=query)
        )
        return object_list

class NewsListView(ListView):
    model = News
    template_name = 'main/news_list.html'

    def get_queryset(self):
        queryset = super(NewsListView, self).get_queryset()
        return queryset

    def get_context_data(self, **kwargs):
        context = super(NewsListView, self).get_context_data()
        context['news_list'] = News.objects.order_by('-id')
        return context


def news_detail_view(request, news_id):
    news = News.objects.get(id=news_id)

    return render(request, 'main/news.html',
                  context={
                      'news': news,
                  })
