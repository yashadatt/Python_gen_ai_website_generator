from django.shortcuts import render, HttpResponse, redirect
from .forms import WebsiteDataForm,AuthorForm,BookForm, ReviewForm
# Create your views here.


def index(request):
    return render(request, 'home.html')


def add_website(request):
    form = WebsiteDataForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request, 'form.html', {'form': form, 'title': 'Add Website'})

def add_author(request):
    form = AuthorForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request, 'form.html', {'form': form, 'title': 'Add Author'})

def add_book(request):
    form = BookForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request, 'form.html', {'form': form, 'title': 'Add Book'})

def add_review(request):
    form = ReviewForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request, 'form.html', {'form': form, 'title': 'Add Review'})


# def index(request):
#     if request.method=='POST':
#         form = WebsiteDataForm(request.POST)
#         if form.is_valid():
#             form.save(commit=True)
#             return redirect('/')
#         # website = request.method.get('website')
#         # website_url = request.method.get('website_url')
#         # website_author = request.method.get('website_author')
#     else:
#         form = WebsiteDataForm()
#     return render(request, 'form.html', {'form': form})



