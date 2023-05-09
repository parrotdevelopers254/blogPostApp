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
    return HttpResponse(f"You are viewing {slug}")

def contact(request):
    return render(request, 'contact.html')

def search(request):
    return render(request, 'search.html')
