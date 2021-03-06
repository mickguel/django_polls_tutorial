from django.urls import path, re_path

from . import views

app_name = 'catalog'
urlpatterns = [
    re_path(r'^$', views.index, name='index'), # path con RegEx
    re_path(r'^book/(?P<pk>\d+)$', views.BookDetailView.as_view(), name='book-detail'), # path con RegEx
    path('books/', views.BookListView.as_view(), name='books'), #path with simple string
    path('authors/', views.AuthorListView.as_view(), name='authors'), #path with simple string
    path('author/<int:pk>', views.AuthorDetailView.as_view(), name='author-detail'), #path with simple string
    re_path(r'^mybooks/$', views.LoanedBooksByUserListView.as_view(), name='my-borrowed'), # path con RegEx
    re_path(r'^borrowed/$', views.LoanedBooksAllListView.as_view(), name='all-borrowed'), # path con RegEx
    re_path(r'^book/(?P<pk>[-\w]+)/renew/$', views.renew_book_librarian, name='renew-book-librarian'), # path con RegEx
    re_path(r'^author/create/$', views.AuthorCreate.as_view(), name='author_create'),
    re_path(r'^author/(?P<pk>\d+)/update/$', views.AuthorUpdate.as_view(), name='author_update'),
    re_path(r'^author/(?P<pk>\d+)/delete/$', views.AuthorDelete.as_view(), name='author_delete'),
]
