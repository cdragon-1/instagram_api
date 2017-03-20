"""
- Class-based view로
    PostList, PostDetail, PostCreate, PostDelete뷰를 작성
        (내용없음)


"""
from django.views import View
from django.views.generic import DetailView
from django.views.generic import ListView

from post.models import Post

__all__ = (
    'PostList',
    'PostDetail',
    'PostDelete',
)


class PostList(ListView):
    model = Post
    context_object_name = 'posts'


class PostDetail(DetailView):
    model = Post

    # def get_context_data(self, **kwargs)::
    # context = post(ArticleDetailView, self).get_context_data(**kwargs)
    # return context


class PostDelete(View):
    pass
