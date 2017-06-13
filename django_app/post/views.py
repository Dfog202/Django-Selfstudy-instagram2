from django.shortcuts import render
from .models import Post


def post_list(request):
    posts = Post.objects.order_by('-create_date')
    context = {
        'posts': posts
    }
    return render(request, 'post/post_list.html', context)
