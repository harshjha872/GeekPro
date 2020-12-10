from django.shortcuts import render,get_object_or_404
from django.views.generic import ListView,DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.contrib.auth.models import User

# Create your views here.

from .models import Article,Contact

class ArticleListView(ListView):
    model=Article
    template_name='home.html'
    ordering=['-date_added']
    paginate_by=4


class AuthorArticleListView(ListView):
    model=Article
    template_name='author_posts.html'
    ordering=['-date_added']
    paginate_by=4

    def get_queryset(self):
        user=get_object_or_404(User,username=self.kwargs.get('username'))
        return Article.objects.filter(author=user).order_by('-date_added')



class ArticleDetailView(DetailView):
    model=Article
    template_name='detail.html'


class ArticleCreateView(LoginRequiredMixin,CreateView):
    model=Article
    fields=['title','image','content']
    template_name='article_new.html'

    def form_valid(self,form):
        form.instance.author=self.request.user
        return super().form_valid(form)



class ArticleUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model=Article
    fields=['title','image','content']
    template_name='article_edit.html'

    def form_valid(self,form):
        form.instance.author=self.request.user
        return super().form_valid(form)

    def test_func(self):
        post=self.get_object()
        if self.request.user==post.author:
            return True
        return False



class ArticleDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model=Article
    template_name='article_delete.html'
    success_url=reverse_lazy('home')

    
    def test_func(self):
        post=self.get_object()
        if self.request.user==post.author:
            return True
        return False

class ContactView(CreateView):
    model=Contact
    fields='__all__'
    template_name='contact.html'

def about(request):
    return render(request,'about.html')