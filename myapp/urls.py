from django.urls import path
from . import views

urlpatterns = [
    path('', views.ArticleListView.as_view(), name='article_list'),
    path('article/<int:pk>', views.ArticleDetailView.as_view(), name='article_view'),
    path('hello/', views.hello_world),
    #path('author/create', views.create_author),
    path('article/create', views.ArticleCreateView.as_view(), name='article_create'),
    path('article/<int:pk>/update', views.ArticleUpdateView.as_view(), name='article_update'),
    path('article/<int:pk>/delete', views.delete_article),
    path('article/<int:pk>/<slug:slug>', views.show_article),
    path('home/', views.home),
    path('about/', views.about)
]


