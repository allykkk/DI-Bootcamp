"""
URL configuration for gif_site project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from gifs.views import (
    HomepageView,
    AddGifView,
    AddCategoryView,
    CategoryView,
    CategoriesView,
    GifsView,
    GifView,
    plus_like, minus_like, popular_gifs_view
)




urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomepageView.as_view(), name='homepage'),
    path('add-gif/', AddGifView.as_view(), name='add-gif'),
    path('add-category/', AddCategoryView.as_view(), name='add-category'),
    path('category/<int:category_id>/', CategoryView.as_view(), name='category'),
    path('categories/', CategoriesView.as_view(), name='categories'),
    path('gifs/', GifsView.as_view(), name='gifs'),
    path('gif/<int:gif_id>/', GifView.as_view(), name='gif'),
    path('gif/<int:gif_id>/plus-likes/', plus_like, name='plus-likes'),
    path('gif/<int:gif_id>/minus-likes/', minus_like, name='minus-likes'),
    path('popular-gifs/', popular_gifs_view, name='popular-gifs'),
    path('accounts/',include('accounts.urls'))
]
