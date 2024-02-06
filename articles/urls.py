from django.urls import path
from . import views
urlpatterns = [
    path('',views.home),
    path('search',views.search_article),
    path('about',views.about),
    path('category/<int:pk>',views.category),
    path('article/<int:pk>',views.article),
    path('createarticles',views.createarticles),
    path('not-found',views.not_found),
    path('del-item/<int:pk>', views.del_from_article),
    path('register', views.Register.as_view())


]