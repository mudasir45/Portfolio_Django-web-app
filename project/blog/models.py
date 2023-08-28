from django.db import models

class Tags(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.name

class Post(models.Model):
    headline = models.CharField(max_length=200)
    sub_headline = models.CharField(max_length=200, null=True, blank=True)
    # thumbnail = 
    body = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=False)
    featured = models.BooleanField(default=False)
    tags = models.ManyToManyField(Tags, blank=True)
    # slug = 

    def __str__(self) -> str:
        return self.headline
    