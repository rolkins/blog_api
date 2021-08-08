from django.db import models
from mptt.models import MPTTModel, TreeForeignKey


class Article(models.Model):
    title = models.CharField(max_length=120)
    text = models.TextField()
    pub_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Comment(MPTTModel):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comment_to_article')
    parent = TreeForeignKey('self', on_delete=models.CASCADE, related_name='reply_to_comment', blank=True, null=True)
    text = models.TextField()
    pub_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.text
