from django.urls import path
from blogapp import views

#app_name='blogapp'

urlpatterns = [
    path('about/',views.AboutView.as_view(),name='about'),
    path('',views.PostListView.as_view(),name='post-list'),
    path('post/(?P<pk>\d+)/',views.PostDetailView.as_view(),name='post-detail'),
    path('post/new/',views.PostCreateView.as_view(),name='new-post'),
    path('post/(?P<pk>\d+)/edit',views.PostUpdateView.as_view(),name='post-update'),
    path('post/(?P<pk>\d+)/remove',views.PostDeleteView.as_view(),name='post-delete'),
    path('drafts/',views.DraftsListView.as_view(),name='drafts'),
    path('post/(?P<pk>\d+)/comment/',views.add_comment_to_post,name='add-comment'),
    path('comment/(?P<pk>\d+)/approve/',views.approve_comment,name='approve-comment'),
    path('post/(?P<pk>\d+)/publish/',views.publish,name='publish-post'),
    path('comment/(?P<pk>\d+)/remove/',views.remove_comment,name='delete-comment'),

]
