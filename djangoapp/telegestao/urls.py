
from django.urls import path
from telegestao.views import index

app_name = 'telegestao'

urlpatterns = [
    path('', index, name='index'),
]

