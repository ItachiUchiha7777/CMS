from django.urls import path    
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('detail/<str:slug>', views.detail, name="detail")
    ,path("create/",views.CreatePost, name="create"),
    path('update-post/<str:slug>',views.UpdatePost,name="update"),
    path('delete-post/<str:slug>',views.DeletePost,name="delete"),
    
]
