from django.core.management.base import BaseCommand
from blogapp.models import Category, Post, Tag

class Command(BaseCommand):

    def handle(self, *args, **options):
        categories= Category.objects.all
        print (categories)
        print(type(categories))
        for item in categories:
            print(item)
            print(type(item))

    #     print('end')
    #
    # category= Category.objects.get(name="Category")
    # print(category)
    # print(type(category))
    # #
    # category = Category.objects.filter(name="Category")
    # print(category)
    # print(type(category))
    #
    # posts=Post.objects.first()
    # print(post)
    #
    #  print(post.category)
    #  print(type(post.category))
    #  print(post.category.name)
    #
    # print(post.tags.all)
    # print(post.tags.first())
    # print(post.tags.first().name)
    # print(type(post.tags.first()))
    #
    # Category.objects.create(name="Новая")
    # Category.name="Измененная"
    # category.save()
    #
    # category.delete()
    # category.objects.all
