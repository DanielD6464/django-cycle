from django.urls import path
from . import views
# from .views import index_view

app_name = 'the_app'
urlpatterns = [
    path('index/', views.index_view, name='index'),
    # path('index/', index_view, name='index'),
]