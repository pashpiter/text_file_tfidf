from django.urls import path
from text_handler import views


app_name: str = 'posts'

urlpatterns = [
    path('', views.index, name='index'),
    path('good', views.index, name='good')
]
