import psycopg2
from psycopg2 import sql

class BookService(library_pb2_grpc.BookServiceServicer):
    def __init__(self):
        self.connection = psycopg2.connect(
            dbname='your_db', user='your_user', password='your_password', host='localhost'
        )
        self.cursor = self.connection.cursor()
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS books (
                id SERIAL PRIMARY KEY,
                title TEXT,
                author TEXT
            )
        """)
        self.connection.commit()

    def CreateBook(self, request, context):
        self.cursor.execute("""
            INSERT INTO books (id, title, author) VALUES (%s, %s, %s)
        """, (request.id, request.title, request.author))
        self.connection.commit()
        return library_pb2.BookResponse(message="Book created")

    def GetBook(self, request, context):
        self.cursor.execute("SELECT title, author FROM books WHERE id = %s", (request.id,))
        row = self.cursor.fetchone()
        if row:
            return library_pb2.Book(id=request.id, title=row[0], author=row[1])
        context.set_details('Book not found')
        context.set_code(grpc.StatusCode.NOT_FOUND)
        return library_pb2.Book()

    def UpdateBook(self, request, context):
        self.cursor.execute("""
            UPDATE books SET title = %s, author = %s WHERE id = %s
        """, (request.title, request.author, request.id))
        self.connection.commit()
        return library_pb2.BookResponse(message="Book updated")

    def DeleteBook(self, request, context):
        self.cursor.execute("DELETE FROM books WHERE id = %s", (request.id,))
        self.connection.commit()
        return library_pb2.BookResponse(message="Book deleted")