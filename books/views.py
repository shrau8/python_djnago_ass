from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Book
from .forms import BookForm
from django.contrib import messages


@login_required
def book_list(request):
    books = Book.objects.all()
    return render(request, 'books/book_list.html', {'books': books})


@login_required
def book_create(request):
    if not request.user.is_admin:
        return redirect('book_list')

    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            book = form.save(commit=False)
            book.added_by = request.user
            book.save()
            messages.success(request, 'Book added successfully!')
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'books/book_form.html', {'form': form})


@login_required
def book_update(request, pk):
    if not request.user.is_admin:
        return redirect('book_list')

    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            messages.success(request, 'Book updated successfully!')
            return redirect('book_list')
    else:
        form = BookForm(instance=book)
    return render(request, 'books/book_form.html', {'form': form})


@login_required
def book_delete(request, pk):
    if not request.user.is_admin:
        return redirect('book_list')

    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        messages.success(request, 'Book deleted successfully!')
        return redirect('book_list')
    return render(request, 'books/book_confirm_delete.html', {'book': book})