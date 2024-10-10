from django.contrib import admin
from django.urls import path
from text_handler.urls import urlpatterns as doc_urls


urlpatterns = [
    path('admin/', admin.site.urls),
]

urlpatterns += doc_urls
