from django.db import models

# Create your models here.
# DB와 연결되는 파이썬 클래스를 models라고 한다

class Post(models.Model):
    title = models.CharField(max_length=32)
    user = models.CharField(max_length=32)
    content = models.TextField()
    region = models.CharField(max_length=16)
    price = models.IntegerField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)