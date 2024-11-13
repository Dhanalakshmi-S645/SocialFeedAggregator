from django.db import models



class Feed(models.Model):
    platform = models.CharField(max_length=100)
    content = models.TextField()
    author = models.CharField(max_length=100)
    timestamp = models.DateTimeField()
    url = models.URLField()

    def __str__(self):
        return f"{self.platform} - {self.author}"
