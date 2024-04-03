from django.shortcuts import render
from .models import Book, Author, BookInstance, Genre, Language
# Create your views here.


def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()

    # Available books (status = 'a')
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()

    # The 'all()' is implied by default.
    num_authors = Author.objects.count()

    # Generate count of books that contain the word 'war' in the title
    num_books_contain_war = Book.objects.filter(title__contains='war').count
    # Generate count of genres that contain the word 'fiction' in the name
    num_genres_contain_fiction = Genre.objects.filter(name__contains='fiction').count

    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
        'num_books_contain_war': num_books_contain_war,
        'num_genres_contain_fiction': num_books_contain_war,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)


from django.views import generic

class BookListView(generic.ListView):
    model = Book
    # Pagination is used to prevent long load times
    paginate_by = 5
    # An example of changing the query to return 5 books containing 'war' in the title
    # def get_queryset(self):
    #     return Book.objects.filter(title__icontains='war')[:5]

    # An example showing how to add a variable 'some_data' to the context
    # def get_context_data(self, **kwargs):
    #     context = super(BookListView, self).get_context_data(**kwargs)
    #     context['some_data'] = 'This is just some data'
    #     return context
    
class BookDetailView(generic.DetailView):
    model = Book

class AuthorListView(generic.ListView):
    model = Author

class AuthorDetailView(generic.DetailView):
    model = Author