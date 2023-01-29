from blogapp.models import Category, Post, Tags

Category.objects.all()
Category.objects.filter(pk=1)

Post.objects.filter(name="tank")
Post.objects.exclude(name="tank")
Post.objects.filter(name="tank", text="ddd")

tanks=Post.objects.filter(name="tank")
some=tanks.filter(text="ddd")
some
tanks=Post.objects.filter(name="tank").filter(text="ddd").filter(name="gggg").exclude(text="ddd")
tanks

tanks=Post.objects.filter(name='tank')
result=tanks.filter(text="ddd")
print(result)


Post.object.filter(rating=3)
Post.object.filter(rating__gt=3)
Post.object.filter(rating__lt=3)
Post.object.filter(rating__lte=3)

Post.object.filter(rating__in=[3,4])
Post.object.filter(name__startswith='ta')
Post.object.filter(name__contains='nk')

import datetime
some_date=datetime.datetime(year=2000, month=1, day=1)
Post.objects.filter(create__gt=some_date)

Post.objects.filter(create__year=2000, create__day=1, create__month=1)
Post.objects.filter(create__in=[some_date])

# получить посты с категорией cars
# с помощью Питона
cars=Category.objects.get(name='cars')
Post.object.filter(category=cars)
# вариант на orm

Post.objects.filter(Category__name="cars")

# Получить посты, которые начинаются на ca
Post.objects.filter(Category__name__startswith="ca")

Goods.objects.filter(shop_city_country_president_wife_name="Kate")


