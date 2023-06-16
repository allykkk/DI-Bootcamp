from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .models import Book, BookReview
from django.views.generic import TemplateView, ListView, View
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView
from .forms import SignUpForm
from django.contrib.auth.views import LoginView, LogoutView


def homepage(request):
    return render(request, 'homepage.html')


# class BookSearchView(ListView):
#     model = Book
#     template_name = "book_search.html"
#
#     def get_queryset(self):
#         query = self.request.GET.get('q')
#         print(query)
#         if query:
#             object_list = self.model.objects.filter(title__icontains=query)
#         else:
#             object_list = self.model.objects.none()
#         return object_list


class BookSearchView(View):
    def get(self, request):
        query = request.GET.get('q')
        books = Book.objects.filter(title__icontains=query)
        return render(request, 'homepage.html', {'books': books, 'query': query})


class BookDetailView(DetailView):
    model = Book
    template_name = "book_detail.html"


class BookListView(ListView):
    model = Book
    template_name = "book_list.html"


class ReviewCreateView(CreateView):
    model = BookReview
    fields = "__all__"
    template_name = "create_review.html"
    success_url = reverse_lazy('search')


class SignUpView(View):
    def get(self, request):
        form = SignUpForm()
        return render(request, 'signup.html', {'form': form})

    def post(self, request):
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('search')
        return render(request, 'signup.html', {'form': form})


class LoginView(LoginView):
    template_name = 'login.html'
    redirect_authenticated_user = True
    next_page='search'


class LogoutView(LogoutView):
    next_page = reverse_lazy('login')
