from rest_framework.pagination import (
LimitOffsetPagination,
PageNumberPagination

)

class PostLimitOffsetPaginnation(LimitOffsetPagination):
     max_limit = 10
     default_limit = 2

class PostPageNumberPagniation(PageNumberPagination):
    page_size = 1