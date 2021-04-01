from django.urls import path
from.views import HomeView,articledetail,Addpost,update,delete,category
from.import views
urlpatterns = [
    path('',HomeView.as_view(),name='home'),
    path('article/<int:pk>',articledetail.as_view(),name='articledetail'),
    path('addpost/',Addpost.as_view(),name='addpost'),
    path('article/edit/<int:pk>',update.as_view(),name='update'),
    path('delete/<int:pk>/remove',delete.as_view(),name='delete'),
    path('category/',category.as_view(),name='category'),
    #path('categories/<str:cats>/',views.categories,name=categories),


]