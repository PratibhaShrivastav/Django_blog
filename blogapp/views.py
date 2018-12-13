from django.shortcuts import render,get_object_or_404,redirect
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from blogapp.models import Post, comments
from django.utils import timezone
from blogapp.forms import Post_form,comment_form
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required

# Create your views here.

class AboutView(TemplateView):
    template_name='about.html'


class PostListView(ListView):
    model=Post

    def query_set(self):
        return Post.objects.filter(publish_date__lte=timezone.now()).order_by('-publish_date')


class PostDetailView(DetailView):
    model=Post


class PostCreateView(LoginRequiredMixin, CreateView):
    login_url= '/login/'
    redirect_field_name='blog/post_detail.html'
    model=Post
    form_class=Post_form


class PostUpdateView(LoginRequiredMixin, UpdateView):
    login_url= '/login/'
    redirect_field_name='blog/post_detail.html'
    model=Post
    form_class=Post_form


class PostDeleteView(LoginRequiredMixin, DeleteView):
    model=Post
    success_url=reverse_lazy('post_list')


class DraftsListView(LoginRequiredMixin, ListView):
    login_url= '/login/'
    redirect_field_name='blog/post_detail.html'
    model=Post

    def query_set(self):
        return Post.objects.filter(publish_date__isnull=True).order_by('-create_date')
    

@login_required
def publish(request,pk):
    post=get_object_or_404(Post,pk=pk)
    post.publish()
    return redirect('post_detail',pk=post.pk)


@login_required
def add_comment_to_post(request,pk):
    post=get_object_or_404(Post,pk=pk)
    if request.method=="POST":
        form=comment_form(request.POST)
        if form.is_valid():
            comment=form.save(commit=False)
            comment.post=post
            comment.save()
    else:
        form=comment_form()

    return render(request,'blog/comment_form',{'form':form})

@login_required
def approve_comment(request,pk):
    comment=get_object_or_404(comments,pk=pk)
    comment.approve()
    return redirect('post_detail',pk=comment.post.pk)

    
@login_required
def remove_comment(request,pk):
    comment=get_object_or_404(comments,pk=pk)
    post_pk=comment.post.pk
    comment.delete()
    return redirect('post_detail',pk=post_pk)










