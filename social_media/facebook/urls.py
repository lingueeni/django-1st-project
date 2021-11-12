from django.urls import path
from .views import posts_list,create_post


urlpatterns = [
    path('posts_list/',posts_list),
    path('create_post/',create_post),

]