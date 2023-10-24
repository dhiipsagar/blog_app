from django.shortcuts import render, get_object_or_404, redirect
from .models import Post

def post_list(request):
    if request.user.is_authenticated:
        posts = Post.published.all()
        return render(request,
                    'blog/post/list.html',
                    {'posts': posts})
    else:
        return redirect('account_login')
    
def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post, slug=post,
    status='published',
    publish__year=year,
    publish__month=month,
    publish__day=day)
    return render(request,
    'blog/post/detail.html',
    {'post': post})