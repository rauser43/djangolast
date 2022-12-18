from django.db import models
from usersapp.models import BlogUser

    # class Meta:
    #     abstract = True


# Create your models here.
class Category(models.Model):
    name= models.CharField(max_length=16, unique=True)
    description= models.TextField(blank=True)

    def __str__(self):
        return self.name

    class TimeStamp(models.Model):
        create = models.DateTimeField(auto_now_add=True)
        update = models.DateTimeField(auto_now=True)

    class Tag(models.Model, TimeStamp):
        name=models.CharField(max_length=16, unique=True)

    def __str__(self):
        return self.name

    class Post(TimeStamp):
        name=models.CharField(max_length=32, unique=True)
        text=models.TextField()


        category=models.ForeignKey(Category, on_delete=models.CASCADE)
        tags=models.ManyToManyField(Tag)
        image=models.ImageField(upload_to='posts', null=True, blank=True)
        user=models.ForeignKey(BlogUser, on_delete=models.CASCADE)

