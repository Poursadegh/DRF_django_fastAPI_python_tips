import grpc
from concurrent import futures
import time
import library_pb2
import library_pb2_grpc

class BookService(library_pb2_grpc.BookServiceServicer):
    def __init__(self):
        self.books = {}

    def CreateBook(self, request, context):
        self.books[request.id] = request
        return library_pb2.BookResponse(message="Book created")

    def GetBook(self, request, context):
        book = self.books.get(request.id)
        if book:
            return book
        context.set_details('Book not found')
        context.set_code(grpc.StatusCode.NOT_FOUND)
        return library_pb2.Book()

    def UpdateBook(self, request, context):
        if request.id in self.books:
            self.books[request.id] = request
            return library_pb2.BookResponse(message="Book updated")
        context.set_details('Book not found')
        context.set_code(grpc.StatusCode.NOT_FOUND)
        return library_pb2.BookResponse()

    def DeleteBook(self, request, context):
        if request.id in self.books:
            del self.books[request.id]
            return library_pb2.BookResponse(message="Book deleted")
        context.set_details('Book not found')
        context.set_code(grpc.StatusCode.NOT_FOUND)
        return library_pb2.BookResponse()

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    library_pb2_grpc.add_BookServiceServicer_to_server(BookService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    try:
        while True:
            time.sleep(86400)
    except KeyboardInterrupt:
        server.stop(0)

if __name__ == '__main__':
    serve()