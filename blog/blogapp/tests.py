from django.test import TestCase
from .models import Post, Category
from usersapp.models import BlogUser
from faker import Faker
from mixer.backend.django import mixer



class PostTestCase(TestCase):

    def setUp(self):
        category = Category.objects.create(name="test_category")
        user = BlogUser.objects.create_user(username="test_user", email="test@test.com", password="leo1234567")

        self.post_str = Post.objects.create(name="test_post_str", text="some", user=user, category=category)

    def test_has_image(self):
        self.assertFalse(self.post.has_image())

    def test_some_method(self):
        post = Post.objects.get(name='test_category')
        self.assertFalse(post.some_method() == ' some method')

    def __str__(self):
        self.assertEqual(str(self.post_str), 'test_post_str, category: test_category')


    class PostTestCaseFake (TestCase):

    def setUp(self):
        faker = Faker()
        category = Category.objects.create(name=faker.name())
        user = BlogUser.objects.create_user(username=faker.name(), email="test@test.com", password="leo1234567")
        self.post = Post.objects.create(name=faker.name(), text=faker.name(), user=user, category=category)

        print(self.post.name)
        print(category.name)

        category = Category.objects.create(name='test.category')
        self.post_str = Post.objects.create(name="test_post_str", text="some", user=user, category=category)

    def test_has_image(self):
        self.assertFalse(self.post.has_image())

    def test_some_method(self):
        self.assertFalse(self.post.some_method() == ' some method')

    def __str__(self):
        self.assertEqual(str(self.post_str), 'test_post_str, category: test_category')

class PostTestCaseMixer(TestCase):

    def setUp(self):
        self.post = mixer.blend (Post)
        # print('mixer-name', self.post.name)
        # print('mixer-category', self.post.category)
        # print('mixer-category-type', type(self.post.category))
        # print('mixer-user-email', self.post.user.email)

        category = mixer.blend(Category,name='test.category')
        self.post_str = mixer.blend(Post, name="test_post_str", category=category)

    self.post_str = mixer.blend(Post, name="test_post_str", category__name= "test_category)

    def test_has_image(self):
        self.assertFalse(self.post.has_image())

    def test_some_method(self):
        self.assertFalse(self.post.some_method() == ' some method')

    def __str__(self):
        self.assertEqual(str(self.post_str), 'test_post_str, category: test_category')


