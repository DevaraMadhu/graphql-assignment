from django.db import models

# Create your models here.

class BlogPost(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    publish_date = models.DateTimeField(auto_now_add=True)
    author  = models.TextField(max_length=100)

    def __str__(self):
        if self.author:     
            return self.author
        else:
            return '-'


class Comments(models.Model):
    comment = models.CharField(max_length=100)
    created_on = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(BlogPost,blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.comment +"  "+ self.author.author
    