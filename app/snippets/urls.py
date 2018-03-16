from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

app_name = 'snippets'

urlpatterns = [

    path('', views.SnippetList.as_view(), ),
    path('<int:pk>/', views.SnippetDetail.as_view(), name=''),
]

urlpatterns = format_suffix_patterns(urlpatterns)