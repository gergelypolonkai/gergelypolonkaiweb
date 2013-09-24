from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    user = models.ForeignKey(User)
    created_at = models.DateTimeField()
    title = models.CharField(max_length = 100)
    slug = models.CharField(max_length = 100)
    content = models.TextField()
    draft = models.BooleanField()

    def __unicode__(self):
        return self.title
