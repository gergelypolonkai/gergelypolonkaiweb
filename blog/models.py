from django.db import models
from django.contrib.auth.models import User
from taggit.managers import TaggableManager

class Post(models.Model):
    user = models.ForeignKey(User)
    created_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length = 100)
    slug = models.SlugField(editable=False, max_length = 100)
    content = models.TextField()
    draft = models.BooleanField()
    tags = TaggableManager()

    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.title)

        super(Post, self).save(*args, **kwargs)
