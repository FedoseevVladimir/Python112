from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='blog/images/')

    def __str__(self):
        return self.title


class Myblog(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True, db_index=True)
    content = models.TextField(blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Мой Блог'
        verbose_name_plural = 'Мои Блоги'