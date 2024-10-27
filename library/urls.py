# library/urls.py

from django.urls import path
from .views import ebook_list, ebook_detail, upload_ebook

urlpatterns = [
    path('', ebook_list, name='ebook_list'),
    path('upload/', upload_ebook, name='upload_ebook'),
    path('ebook/<int:ebook_id>/', ebook_detail, name='ebook_detail'),
]
