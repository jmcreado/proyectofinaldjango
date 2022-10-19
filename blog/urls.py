from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),

    path('posts/<int:pk>', views.post_show, name='post.show'),
    path('posts/listar', views.post_list, name='post.list'),
    path('posts/crear', views.post_create, name='post.create'),

    path('categories/listar', views.category_list, name='category.list'),
    path('categories/crear', views.category_create, name='category.create'),

    path('profiles/listar', views.profile_list, name='profile.list'),
    path('profiles/<int:pk>', views.profile_show, name='profile.show'),

    path('users/crear', views.user_create, name='user.create'),
    path("register", views.register_request, name="register"),
    path('login', views.auth_login, name='login'),
    path('logout', views.auth_logout, name='logout'),
]
