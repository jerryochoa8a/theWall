from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('reg', views.reg),
    path('login', views.login),
    path('logout', views.logout),
    path('home',views.home),
    path('home/post_mes', views.post_mes),
    path('the_wall', views.the_wall),
    path('the_wall/post_com/<mess_id>', views.post_com)
]