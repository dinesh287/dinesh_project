from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import All_books, All_users


# Create your views here.


def handle_login(request):
    if request.method == 'POST':
        # email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'successfully logged in')
            return redirect('dashboard')
        else:
            messages.warning(request, 'wrong credentials')
    return render(request, 'handle_login.html')


def dashboard(request):
    books = All_books.objects.all()
    context = {
        'books': books
    }
    return render(request, 'dashboard.html', context)


def handle_logout(request):
    logout(request)
    messages.success(request, 'successfully log out')
    return redirect('handle_login')


def handle_signup(request):
    if request.method == 'POST':
        if request.POST['username'] and request.POST['email'] and request.POST['password']:
            saverecord = All_users()
            saverecord.username = request.POST['username']
            saverecord.email = request.POST['email']
            saverecord.password = request.POST['password']
            saverecord.save()
            messages.success(request, 'successfully register')
            return redirect('handle_login')
    return render(request, 'handle_signup.html')


@login_required()
def add_book(request):
    if request.method == 'POST':
        book_id = request.POST['book_id']
        book_name = request.POST['book_name']
        book_author = request.POST['book_author']
        book_desc = request.POST['book_desc']
        book = All_books(book_id=book_id, book_name=book_name, book_author=book_author, book_desc=book_desc)
        book.save()
        messages.success(request, 'successfully added book')
        return redirect('dashboard')

    return render(request, 'add_book.html')


@login_required()
def delete_book(request, pk):
    book = All_books.objects.get(id=pk)
    book.delete()
    messages.success(request, 'successfully deleted')
    return redirect('dashboard')


@login_required()
def update_book(request, pk):
    book = All_books.objects.get(id=pk)
    context = {
        'book': book
    }
    if request.method == 'POST':
        book.book_id = request.POST['book_id']
        book.book_name = request.POST['book_name']
        book.book_author = request.POST['book_author']
        book.book_desc = request.POST['book_desc']
        book.save()
        messages.success(request, 'successfully updated')
        return redirect('dashboard')
    return render(request, 'update_book.html', context)


@login_required()
def view_book(request, pk):
    book = All_books.objects.get(id=pk)
    context = {
        'book': book
    }
    return render(request, 'view_book.html', context)
