from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from urls import views

urlpatterns = [
    path('urls/', views.url_add),
    path('<str:pk>/', views.url_redirect),
]

urlpatterns = format_suffix_patterns(urlpatterns)
