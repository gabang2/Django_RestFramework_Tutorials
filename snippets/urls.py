from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from snippets import views

urlpatterns = [
    path('snippets/', views.snippet_list),
    path('snippets/<int:pk>/', views.snippet_detail)
]

# url 뒤에 .json등 확장자 정보를 붙여 확장자를 받아올 수 있음
urlpatterns = format_suffix_patterns(urlpatterns)
