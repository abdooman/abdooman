from django.shortcuts import render , redirect
from django.http import HttpResponse
from myapp.models import Author, Article
from django.core.exceptions import ObjectDoesNotExist
from myapp.forms import ArticleForm
from django.views.generic import ListView, DetailView, FormView, CreateView, UpdateView
from django.urls import reverse, reverse_lazy
# Create your views here.


def hello_world(request):
    #fetch data from database
        return render(request,"hello.html", {
            'name': 'abdooma',
            'categories': [
                'Category 1',
                'Category 2',
                'Category 3'
            ]
        })

def show_article(request, id, slug):
    return HttpResponse('Article ' + str(id) + str(slug))

    
def home(request):
    #author = Author()
    #author.name = 'Abdullrhman'
    #author.email = 'maan1020@hotmail.com'
    #Author.objects.create(
   #    name='Abdullatif', email='Abd@gmail.com'
   # )
    article = Article()
    article.title = 'Python Article'
    article.content = 'Python article content here.'
    article.author = Author(1)
    article.save()

    #author.save()

    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


#def articles(request):
    #امر الترتيب order_by
    #وهناك امر first and last
    # gt = greater than اكبر من 
    #gte = greater than or equal اكبر من او يساوي 
    #lt = less than اصغر من 
    #lte = less than orr equal اصغر من او يساوي   
    #range للمقارانة بين العناصر 
    # لتفعيل العناصر نضع pk__ ثم نضيف العنصر المراد 
#   models = Article.objects.order_by('id')
#    return render(request, 'article/list.html', {
#        'articles': models
#    })



def show_article2(request, id):
    model = Article.objects.filter(pk=id).first()
    return render(request, 'article/show.html', {
        'article': model
    })

def create_article(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            content = form.cleaned_data['content']
            author = form.cleaned_data['author']
            tags = form.cleaned_data['tags']
            article = Article.objects.create(title=title, content=content, author=author)
            article.tags.set(tags)
            return redirect('/myapp/')
    else:
        form = ArticleForm()
    return render(request, 'article/create.html', {
        'form': form
    })
    

def update_article(request, pk):
    article = Article.objects.get(pk=1)
    article.title = 'New Title'
    article.save()
    return render(request, 'article/show.html',{
        'article': article
    })

def delete_article(request, pk):
    article = Article.objects.get(pk=pk)
    article.delete()
    return redirect(request, '/myapp/')

#def create_author(request):
#    if request.method == 'POST':
#        form = AuthorForm(request.POST)
#        if form.is_valid():
#            Author.objects.create(
#                name=form.cleaned_data['name'],
#                email=form.cleaned_data['email'],
#                birthdate=form.cleaned_data['birthdate'],
#                bio=form.cleaned_data['bio']
#            )
#            return redirect('/myapp/')
#    else:
#        form = AuthorForm()
#    return render(request, 'author/create.html', {
#        'form': form
#    })

class ArticleListView(ListView):
    model = Article 
    template_name = 'article/list.html'
    queryset = Article.objects.select_related('author').prefetch_related('tags')

class ArticleDetailView(DetailView):
    model = Article
    template_name = 'article/show.html'

#class ArticleCreateView(FormView):
#    form_class = ArticleForm
#    template_name = 'article/create.html'
    
#    def get_success_url(self):
#        return reverse('article_list')
#
#    def form_valid(self, form):
#        article = Article.objects.create(
#            title=form.cleaned_data['title'],
#            content=form.cleaned_data['content'],
#            author=form.cleaned_data['author']
#        )
#        article.tags.set(form.cleaned_date['tags'])
#       return super().form_valid(form)

class ArticleCreateView(CreateView):
    model = Article 
    form_class = ArticleForm
    template_name = 'article/create.html'
    success_url = reverse_lazy('article_list')
    
 

class ArticleUpdateView(UpdateView):
    model = Article    
    template_name = 'article/update.html'
    fields = ['title', 'content', 'author']

    def get_success_url(self):
        return reverse('article_list')
 