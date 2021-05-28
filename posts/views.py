from django.shortcuts import render
from .models import Post
from django.http import JsonResponse

# Create your views here.

def home_view(request):
    qs = Post.objects.all()
    context = {
        'hello': 'hello world',
        'qs': qs,
    
    }
    return render(request, 'posts/main.html', context)

def post_view_json(request):
    qs = Post.objects.all()
    return JsonResponse({'data':qs})