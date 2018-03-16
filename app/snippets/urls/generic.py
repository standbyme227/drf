from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from ..apis.generic import SnippetDetail, SnippetList

urlpatterns = [

    path('', SnippetList.as_view(), ),
    path('<int:pk>/', SnippetDetail.as_view(), name=''),
]

urlpatterns = format_suffix_patterns(urlpatterns)
