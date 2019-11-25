from django.db import models

# Create your models here.
class Comment(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    comment = models.TextField()
    name = models.CharField(max_length=100)

    class Meta:
        ordering = ['created']

    def __str__(self):
        return self.created.strftime('%m/%d/%Y') + ' ' + self.name