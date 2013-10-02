from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
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

class CodeChunk(models.Model):
    language = models.CharField(max_length = 20)
    created_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length = 100)
    slug = models.SlugField(editable = False, max_length = 100)
    description = models.TextField(blank=True)
    content = models.TextField()

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.title)

        super(CodeChunk, self).save(*args, **kwargs)

