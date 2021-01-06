from django.db import models

# Create your models here.
class Post(models.Model):
    post_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255, unique=True)
    author = models.CharField(max_length=80)
    content = models.TextField()
    slug = models.CharField(max_length=255)
    timestamp = models.DateTimeField()

    def __str__(self):
        return self.title + " by " + self.author