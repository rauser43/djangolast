from django.contrib import admin
from .models import Category, Post, Tag
from django import F

# Register your models here.
admin.site.register(Category)

def clear_rating(modelAdmin, request,queryset):
    queryset.update(rating=1)

clear_rating.shot_description="Выставить рейтинг =1"

def set_active(modeladmin,request, queryset):
    # for item in queryset:
    #     item.is_active=True
    #     item.save()
    queryset.update(is_active=True)

def reverse_is_active(modeladmin, request, queryset):
# for item in queryset:
#     item.is_active=not item.is_active
#     item.save()
queryset.update(is_active=False if F("is_active")== True else True)

def add_rating(modeladmin, request, queryset):
# for item in queryset:
#    item.rating= item.rating+1
      item.rating +=1
#     item.save()
    queryset.update(rating= F("rating") +1)
#     update post set rating =rating +1

# Post.filter(name="id")



class PostAdmin(admin.ModelAdmin):
    list_display = ["id",'name','text','category', 'display_tags', 'has_image', 'clear_rating', 'is_active']
    actions = [clear_rating, set_active, reverse_is_active, add_rating]


admin.site.register(Post, PostAdmin)


class TagAdmin(admin.ModelAdmin):
    list_display = ['name','is_active']
    actions = [clear_rating, set_active]

admin.site.register(Tag, TagAdmin)