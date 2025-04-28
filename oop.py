# just review the code and become fresh for python interviews
# polymorphism
import math


class Shape:
    def area(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


shapes = [Circle(5), Rectangle(4, 6)]
for shape in shapes:
    print(shape.area())  # خروجی: 78.53981633974483 و 24


# composition: library is composed of books
class Book:
    def __init__(self, title):
        self.title = title


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def list_books(self):
        for book in self.books:
            print(book.title)


library = Library()
library.add_book(Book("1984"))
library.add_book(Book("Brave New World"))
library.list_books()  # خروجی: 1984, Brave New World


# mixin in python
class JSONMixin:
    def to_json(self):
        import json
        return json.dumps(self.__dict__)


class XMLMixin:
    def to_xml(self):
        xml = '<object>'
        for key, value in self.__dict__.items():
            xml += f'<{key}>{value}</{key}>'
        xml += '</object>'
        return xml


# mixin usage
class User(JSONMixin, XMLMixin):
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Product(JSONMixin):
    def __init__(self, title, price):
        self.title = title
        self.price = price


user = User("Alice", 30)
product = Product("Laptop", 1200)

print(user.to_json())  # خروجی: {"name": "Alice", "age": 30}
print(user.to_xml())  # خروجی: <object><name>Alice</name><age>30</age></object>

print(product.to_json())  # خروجی: {"title": "Laptop", "price": 1200}


# Dependency Injection

# 1-no DI

class Database:
    def connect(self):
        return "Connected to the database"


class UserService:
    def __init__(self):
        self.database = Database()  # وابستگی به Database

    def get_user(self):
        return self.database.connect()


# استفاده
user_service = UserService()
print(user_service.get_user())  # خروجی: Connected to the database


# 2- DI usage


class Database:
    def connect(self):
        return "Connected to the database"


class UserService:
    def __init__(self, database):
        self.database = database  # وابستگی از بیرون تزریق می‌شود

    def get_user(self):
        return self.database.connect()


# استفاده
database = Database()
user_service = UserService(database)  # وابستگی به Database تزریق می‌شود
print(user_service.get_user())  # خروجی: Connected to the database


# انواع di


# 1- Constructor Injection
class Database:
    def connect(self):
        return "Connected to the database"


class UserService:
    def __init__(self, database: Database):
        self.database = database


# استفاده
db = Database()
user_service = UserService(db)


# 2-setter /getter
class UserService:
    def __init__(self):
        self.database = None

    def set_database(self, database: Database):
        self.database = database


# استفاده
user_service = UserService()
user_service.set_database(Database())


# 3- Interface Injection
class DatabaseInterface:
    def connect(self):
        raise NotImplementedError


class Database(DatabaseInterface):
    def connect(self):
        return "Connected to the database"


class UserService:
    def __init__(self, database: DatabaseInterface):
        self.database = database


# استفاده
db = Database()
user_service = UserService(db)


# 4-  Service Locator
class ServiceLocator:
    _services = {}

    @staticmethod
    def register_service(service_name, service):
        ServiceLocator._services[service_name] = service

    @staticmethod
    def get_service(service_name):
        return ServiceLocator._services.get(service_name)


# استفاده
ServiceLocator.register_service('database', Database())
user_service = UserService(ServiceLocator.get_service('database'))

# interface in python
from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def area(self):
        """محاسبه مساحت"""
        pass

    @abstractmethod
    def perimeter(self):
        """محاسبه محیط"""
        pass


# IMPLEMENting interface
import math


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


# diamond problem  - MRO (Method Resolution Order) ?

class A:
    def greet(self):
        print("Hello from A")


class B(A):
    def greet(self):
        super().greet()
        print("Hello from B")


class C(A):
    def greet(self):
        super().greet()
        print("Hello from C")


class D(B, C):
    def greet(self):
        super().greet()  # اینجا MRO به ترتیب صحیح عمل می‌کند


d = D()
d.greet()




