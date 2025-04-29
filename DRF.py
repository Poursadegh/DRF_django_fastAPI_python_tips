# you know that one single file is not runable and is here for the record
# prefetched_related
class BookListView(generics.ListAPIView):
    queryset = Book.objects.select_related('author')
    serializer_class = BookSerializer


class AuthorListView(generics.ListAPIView):
    queryset = Author.objects.prefetch_related('books')
    serializer_class = AuthorSerializer


# select_related
class BookListView(generics.ListAPIView):
    queryset = Book.objects.select_related('author')
    serializer_class = BookSerializer
