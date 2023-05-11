from django.shortcuts import render, HttpResponse
from blogs.models import Blog
# Create your views here.
def home(request):
    return render(request, 'index.html')

def blog(request):
    blogs = Blog.objects.all()
    context = {'blogs': blogs}
    return render(request, 'blogpost.html', context)

def blogPost(request, slug):
    blogs = Blog.objects.filter(slug=slug).first()
    context = {'blogs': blogs}
    return render(request, 'bloghome.html', context)

def contact(request):
    return render(request, 'contact.html')

def search(request):
    return render(request, 'search.html')
