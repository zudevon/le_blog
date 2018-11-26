from django.db import models

# Create your models here.
class Articles(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    # add thumbnail later
    # add author later

    def __str__(self):
        return self.title


    def snippet(self):
        return self.body[:50]+'...'  # returns only the first 50 characters
