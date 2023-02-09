from django.db import models

# Create your models here.
class Author(models.Model): #علاقة واحد الى واحد One To One 
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    birthdate = models.DateField(null=True)
    bio = models.TextField(null=True)

    def __str__(self):
        return self.name+ ' ' + self.email


class Tag(models.Model): # علاقة كثير الى كثير Many To Many 
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name

class Article(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.OneToOneField(Author, on_delete=models.PROTECT)
    #author = models.ForeignKey(Author, on_delete=models.PROTECT)  علاقة واحد الى كثير One To Many
    tags = models.ManyToManyField(Tag, related_name='articles')
