from django.shortcuts import render
from django.views.generic import ListView,DetailView
from .models import Post

# Create your views here.
# def index(request):
#     posts = Post.objects.all().order_by('-pk')
#
#     return render(
#         request,
#         'blog/post_list.html',
#         {
#             'posts':posts,
#         }
#     )

class PostList(ListView): #모델명_list.hmtl
    model = Post #post_list 변수
    # template_name = 'blog/post_list.html' 템플릿 이름 바꾸기
    ordering = '-pk'

def single_post_page(request, pk):
    post = Post.objects.get(pk=pk)

    return render(

        request,
        'blog/single_post_page.html',
        {
            'post':post,
        }
    )