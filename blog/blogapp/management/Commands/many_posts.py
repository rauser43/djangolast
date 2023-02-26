from django.core.management.base import BaseCommand
from mixer.backend.django import mixer

from blogapp.models import Post, Tag, Category
from usersapp.models import BlogUser

class Command(BaseCommand):

    def handle(self, *args, **options):
        Post.оbjects.all().delete()
        Tag.оbjects.all().delete()
        Category.оbjects.all().delete()
        BlogUser.objects.filter(is_superuser=False).delete()

        count=100
        for in range (count):
            p=(i/count)*100
            print(f'{i}) {p} %')
            mixer.blend(Post)

        print('end')