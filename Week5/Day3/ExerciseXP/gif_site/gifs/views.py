from django.shortcuts import render, redirect
from django.views import View
from .forms import GifForm, CategoryForm
from .models import Gif, Category


class HomepageView(View):
    def get(self, request):
        gifs = Gif.objects.all()
        context = {'gifs': gifs}
        return render(request, 'homepage.html', context)


class AddGifView(View):
    def get(self, request):
        form = GifForm()
        context = {'form': form}
        return render(request, 'add_gif.html', context)

    def post(self, request):
        form = GifForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('homepage')
        return render(request, 'add_gif.html', {'form': form})


class AddCategoryView(View):
    def get(self, request):
        form = CategoryForm()
        context = {'form': form}
        return render(request, 'add_category.html', context)

    def post(self, request):
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('categories')
        return render(request, 'add_category.html', {'form': form})


class CategoriesView(View):
    def get(self, request):
        categories = Category.objects.all()
        context = {'categories': categories}
        return render(request, 'categories.html', context)


class GifsView(View):
    def get(self, request):
        gifs = Gif.objects.all()
        context = {'gifs': gifs}
        return render(request, 'gifs.html', context)


class CategoryView(View):
    def get(self, request, category_id):
        category = Category.objects.get(id=category_id)
        gifs = category.gifs.all()
        context = {'category': category, 'gifs': gifs}
        return render(request, 'category.html', context)


class GifView(View):
    def get(self, request, gif_id):
        gif = Gif.objects.get(id=gif_id)
        context = {'gif': gif}
        return render(request, 'gif.html', context)


def plus_like(request, gif_id):
    gif = Gif.objects.get(id=gif_id)
    gif.likes += 1
    gif.save()
    return redirect('gif', gif_id=gif_id)


def minus_like(request, gif_id):
    gif = Gif.objects.get(id=gif_id)
    if gif.likes > 0:
        gif.likes -= 1
        gif.save()
    return redirect('gif', gif_id=gif_id)


def popular_gifs_view(request):
    gifs = Gif.objects.filter(likes__gt=0).order_by('-likes')
    context = {'gifs': gifs}
    return render(request, 'popular_gifs.html', context)
