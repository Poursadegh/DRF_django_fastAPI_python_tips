import grpc
import library_pb2
import library_pb2_grpc

def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = library_pb2_grpc.BookServiceStub(channel)

        # Create a book
        book = library_pb2.Book(id="1", title="1984", author="George Orwell")
        response = stub.CreateBook(book)
        print(response.message)

        # Get a book
        response = stub.GetBook(library_pb2.BookRequest(id="1"))
        print(f'Book: {response.title} by {response.author}')

        # Update a book
        book.title = "Nineteen Eighty-Four"
        response = stub.UpdateBook(book)
        print(response.message)

        # Delete a book
        response = stub.DeleteBook(library_pb2.BookRequest(id="1"))
        print(response.message)

if __name__ == '__main__':
    run()