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


# کش کردن در سطح ویو
from django.views.decorators.cache import cache_page
from rest_framework.decorators import api_view


@api_view(['GET'])
@cache_page(60 * 15)  # کش برای 15 دقیقه
def my_view(request):
    # منطق ویو
    pass


# در سطح سریالایزر
from django.core.cache import cache
from rest_framework import serializers


class MySerializer(serializers.ModelSerializer):
    class Meta:
        model = MyModel
        fields = '__all__'

    def to_representation(self, instance):
        cache_key = f"my_model_{instance.id}"
        data = cache.get(cache_key)

        if not data:
            data = super().to_representation(instance)
            cache.set(cache_key, data, timeout=60 * 15)  # کش برای 15 دقیقه

        return data


# در سطح کوئری ست
from django.core.cache import cache
from rest_framework import viewsets


class MyViewSet(viewsets.ModelViewSet):
    queryset = MyModel.objects.all()
    serializer_class = MySerializer

    def get_queryset(self):
        cache_key = 'my_model_queryset'
        queryset = cache.get(cache_key)

        if not queryset:
            queryset = super().get_queryset()
            cache.set(cache_key, queryset, timeout=60 * 15)  # کش برای 15 دقیقه

        return queryset


# invalidate cache


from django.core.cache import cache


def create(self, request, *args, **kwargs):
    response = super().create(request, *args, **kwargs)
    cache.delete('my_model_queryset')  # خالی کردن کش
    return response


# ورژن زدن برای کش

def get_data(param):
    cache_key = f"dynamic_data_{param}_v{CACHE_VERSION}"
    data = cache.get(cache_key)

    if not data:
        # منطق برای دریافت داده‌های جدید
        data = fetch_data(param)
        cache.set(cache_key, data, timeout=60 * 15)  # کش برای 15 دقیقه

    return data


# clear cache with changing version

from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.core.cache import cache


@receiver(post_save, sender=MyModel)
@receiver(post_delete, sender=MyModel)
def clear_cache(sender, **kwargs):
    global CACHE_VERSION
    CACHE_VERSION += 1  # افزایش نسخه کش
    cache.clear()  # یا فقط کلیدهای وابسته را خالی کنید
