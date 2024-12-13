from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
  path('', views.posts_list, name="list"),
  path('new-post/', views.post_new, name="new_post"),
  path('<slug:post_slug>', views.post_page, name="page"),
]
