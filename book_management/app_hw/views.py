from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from .forms import *
from .models import *
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView


class StartPage(TemplateView):
    template_name = 'app/start_page.html'


class BookList(ListView):
    model = Book
    template_name = 'app/book_list.html'
    context_object_name = 'books'
    extra_context = {'book_list': Book.objects.all()}


class AuthorList(ListView):
    model = Author
    template_name = 'app/author_list.html'
    context_object_name = 'authors'
    extra_context = {'author_list': Author.objects.all()}


class BookDetail(DetailView):
    model = Book
    template_name = 'app/book_detail.html'
    slug_url_kwarg = 'book_slug'
    context_object_name = 'book'


def book_detail_view(request, slug):
    book = get_object_or_404(Book, slug=slug)
    context = {'book': book}

    return render(request, 'app/book_detail.html', context)


class AuthorDetail(DetailView):
    model = Author
    template_name = 'app/author_detail.html'


def author_detail_view(request, slug):
    author = get_object_or_404(Author, slug=slug)
    context = {'author': author}

    return render(request, 'app/author_detail.html', context)


class BookCreate(CreateView):
    model = Book
    form_class = BookForm
    template_name = 'app/book_create.html'
    success_url = reverse_lazy('book_list')


def create_book_view(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()
    context = {'form': form}

    return render(request, 'app/book_create.html', context)


class AuthorCreate(CreateView):
    model = Author
    form_class = AuthorForm
    template_name = 'app/author_create.html'
    success_url = reverse_lazy('author_list')


def create_author_view(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('author_list')
    else:
        form = AuthorForm()
    context = {'form': form}

    return render(request, 'app/author_create.html', context)


class BookUpdate(UpdateView):
    template_name = 'app/book_update.html'
    model = Book
    fields = ('title', 'author', 'year', 'genres', 'rating')
    success_url = reverse_lazy('book_list')


def book_update_view(request, slug):
    book = Book.objects.get(slug=slug)

    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm(instance=book)
    context = {'form': form}

    return render(request, 'app/book_update.html', context)


class AuthorUpdate(UpdateView):
    template_name = 'app/author_update.html'
    model = Author
    fields = ('first_name', 'last_name')
    success_url = reverse_lazy('author_list')


def author_update_view(request, slug):
    author = Author.objects.get(slug=slug)

    if request.method == 'POST':
        form = AuthorForm(request.POST, instance=author)
        if form.is_valid():
            form.save()
            return redirect('author_list')
    else:
        form = AuthorForm(instance=author)
    context = {'form': form}

    return render(request, 'app/author_update.html', context)


class BookDelete(DeleteView):
    template_name = 'app/book_delete.html'
    model = Book
    success_url = reverse_lazy('book_list')


def book_delete_view(request, slug):
    if request.method == 'POST':
        Book.objects.get(slug=slug).delete()

        return redirect('book_list')
    return render(request, 'app/book_delete.html')


class AuthorDelete(DeleteView):
    template_name = 'app/author_delete.html'
    model = Author
    success_url = reverse_lazy('author_list')

