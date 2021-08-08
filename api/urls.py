from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import ArticleList, ArticleDetail, CommentsList, CommentDetail

urlpatterns = [
    path('articles/', ArticleList.as_view()),
    path('articles/<int:pk>/', ArticleDetail.as_view()),
    path('comments/', CommentsList.as_view()),
    path('comments/<int:pk>/', CommentDetail.as_view()),
]