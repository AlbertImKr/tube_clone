from django.contrib.auth.models import User
from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    thumbnail_image = models.ImageField(upload_to='blog/image/%Y/%m/%d/')
    video_file = models.FileField(upload_to='blog/files/%Y/%m/%d/')
    view_count = models.IntegerField(default=0)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    tags = models.ManyToManyField('Tag', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    message = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE,
                             related_name='comments')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.message


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Subscription(models.Model):
    subscriber = models.ForeignKey(
            User, on_delete=models.CASCADE, related_name="subscriptions"
    )
    channel = models.ForeignKey(
            User, on_delete=models.CASCADE, related_name="subscribers"
    )
    subscribed_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("subscriber", "channel")  # 구독자와 채널은 유일해야 함

    def __str__(self):
        return f"{self.subscriber.username}이 {self.channel.username}를 구독하였습니다."
