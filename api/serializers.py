from rest_framework import serializers
from .models import Article, Comment
from rest_framework_recursive.fields import RecursiveField


class CommentSerializer(serializers.ModelSerializer):
    reply_to_comment = RecursiveField(allow_null=True, many=True, read_only=True)

    class Meta:
        model = Comment
        fields = ['id', 'text', 'article', 'reply_to_comment', 'parent']


class ArticleSerializer(serializers.ModelSerializer):
    comment_to_article = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Article
        fields = '__all__'
