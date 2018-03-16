from django.urls import path, re_path, include
from .. import apis

app_name = 'snippets'

urlpatterns = [
    path('api-view/', include('snippets.urls.api_view')),
    path('mixins/', include('snippets.urls.mixins')),
    path('generic/', include('snippets.urls.mixins')),
]
