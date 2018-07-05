from django.db import models
from datetime import datetime
from django.contrib.auth.models import User


class Sections(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=300)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Sections"


class Topics(models.Model):
    section = models.ForeignKey(Sections, on_delete=models.CASCADE, default="")
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=200)
    created_at = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Topics"


class Posts(models.Model):
    topic = models.ForeignKey(Topics, on_delete=models.CASCADE, default="")
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    body = models.TextField(max_length=300)
    created_at = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return(self.author.get_username() + ': ' + self.body)

    class Meta:
        verbose_name_plural = "Posts"
