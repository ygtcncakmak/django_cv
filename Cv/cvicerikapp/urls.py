from django.urls import path
from . import views
    # http://127.0.0.1:8000/             =>index
    # http://127.0.0.1:8000/index        => index
    # http://127.0.0.1:8000/blogs        => blog
    # http://127.0.0.1:8000/blogs/3      => blog-details
    
urlpatterns = [
    path("",views.index,name="homepage"),
    path("index",views.index),
    path("about",views.about),
    path("blogs",views.blogs),
    path("blogs/<int:id>",views.blogs_details),
]
