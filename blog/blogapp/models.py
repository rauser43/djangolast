from django.db import models
from usersapp.models import BlogUser

    # class Meta:
    #     abstract = True
class ActiveManager(models.Manager):

    def get_queryset(self):
        all_objects=super().get_queryset()
        return all_objects.filter(is_active=True)

    class IsActiveMixin(models.Model):
        objects = models.Manager()
        active_objects = ActiveManager()
        is_active=models.BooleanField(default=False)

    class Meta:
        abstract=True

# Create your models here.
class Category(models.Model):
    name= models.CharField(max_length=16, unique=True)
    description= models.TextField(blank=True)

    def __str__(self):
        return self.name

# class UpdatedObjectsManager(models.Manager):
#     def get_queryset(self):
#         all_objects=super().get_queryset()
#         return all_objects.filter(update=?)

    class TimeStamp(models.Model):
        create = models.DateTimeField(auto_now_add=True)
        update = models.DateTimeField(auto_now=True)

    class Tag(IsActiveMixin):
        name=models.CharField(max_length=16, unique=True)

    def __str__(self):
        return f'{self.name}, category: {self.category.name}'

    def display_tags(self):
        tags=self.tags.all()
        result = ';'.join([item.name for item in tags])
        # return result
        return self.name


# class Chiled(ActiveManager):
#     pass

    class Post(TimeStamp, IsActiveMixin):
        objects=models.Manager()
        active_objects=ActiveManager()
        name=models.CharField(max_length=32, unique=True)
        text=models.TextField()


        category=models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category_posts')
        tags=models.ManyToManyField(Tag)
        image=models.ImageField(upload_to='posts', null=True, blank=True)
        user=models.ForeignKey(BlogUser, on_delete=models.CASCADE)
        rating=models.PositiveSmallIntegerField(default=1)
        is_active=models.BooleanField(default=False)


        def has_image(self):
            print("my image:", self.image)
            print("type", type(self.image))
            return self.image is not None

        def some_method(self):
            return "hello from method"
