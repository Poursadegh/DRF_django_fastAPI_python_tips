import re
from django.http import HttpResponseForbidden
import time
from collections import defaultdict


# add to seetings.py
# MIDDLEWARE = [
#     ...
#     'myproject.waf_middleware.WAFMiddleware',
#     ...
# ]


class WAFMiddleware:
    blacklist_patterns = [
        r"(.*)(select|union|insert|delete|update|drop|;|--)(.*)",  # SQL Injection
        r"(.*)(<script>)(.*)",  # XSS
    ]

    # دیکشنری برای پیگیری درخواست‌ها
    request_count = defaultdict(list)
    RATE_LIMIT = 100  # تعداد محدودیت درخواست‌ها
    TIME_WINDOW = 60  # زمان محدودیت در ثانیه

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        ip = request.META.get('REMOTE_ADDR')

        # پاک کردن درخواست‌های قدیمی
        current_time = time.time()
        self.request_count[ip] = [timestamp for timestamp in self.request_count[ip] if
                                  current_time - timestamp < self.TIME_WINDOW]

        # بررسی محدودیت نرخ
        if len(self.request_count[ip]) >= self.RATE_LIMIT:
            return HttpResponseForbidden("Forbidden: Rate limit exceeded")

        # افزودن زمان درخواست جدید
        self.request_count[ip].append(current_time)

        # بررسی الگوهای ناخواسته
        for pattern in self.blacklist_patterns:
            if re.search(pattern, request.body.decode('utf-8'), re.IGNORECASE):
                return HttpResponseForbidden("Forbidden: Unsafe request")

        # بررسی CSRF
        if request.method == "POST":
            token = request.META.get('HTTP_X_CSRF_TOKEN')
            if token != request.COOKIES.get('csrftoken'):
                return HttpResponseForbidden("Forbidden: Invalid CSRF token")

        response = self.get_response(request)
        return response
