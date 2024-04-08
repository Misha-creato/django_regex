from django.urls import path
from regex.views import index_view


urlpatterns = [
    path(
        '',
        index_view,
        name='index'
    )
]
