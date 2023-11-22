from re import TEMPLATE, template
from django.shortcuts import render
from .models import Articles
from django.views.generic import ListView, DetailView
from .Forms import ArticleForm


#def home(request):
#    list_articles = Articles.objects.all()
#    context = {
#        'name': 'Иван',
#        'list_articles':list_articles
#    }
#    template = 'index.html'
#    return render(request, template, context)


class HomeListView(ListView):
    model = Articles
    template_name = 'index.html'
    context_object_name = 'list_articles'


#def detail_page(request, id):
#    get_article = Articles.objects.get(id=id)
#    context = {
#        'get_article':get_article
#        }
#    template = 'detail.html'    
#    return render(request, template, context)


class HomeDetailView(DetailView):
    model = Articles
    template_name = 'detail.html'
    context_object_name = 'get_article'

def edit_page(request):
    template = 'edit_page.html'
    context = {
        'list_articles': Articles.objects.all().order_by('-id'),
        'form': ArticleForm()
        }
    return render(request, template, context)