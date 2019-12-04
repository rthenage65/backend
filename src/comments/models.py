from django.db import models

class Post(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    post = models.TextField()
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=100)
    author = models.CharField(max_length=100)


    class Meta:
        ordering = ['created']

    def __str__(self):
        return self.created.strftime('%m/%d/%Y') + ' ' + self.author

class Comment(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    comment = models.TextField()
    name = models.CharField(max_length=100)

    _post = models.ForeignKey(to=Post, on_delete=models.CASCADE, default=1)

    class Meta:
        ordering = ['created']

    def __str__(self):
        return self.created.strftime('%m/%d/%Y') + ' ' + self.name