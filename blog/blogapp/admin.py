from django.contrib import admin
from .models import Category, Post, Tag

# Register your models here.
admin.site.register(Category)

def clear_rating(modelAdmin, request,queryset):
    queryset.update(rating=1)

clear_rating.shot_description="Выставить рейтинг =1"

def set_active(modeladmin,request, queryset):
    queryset.update(is_active=True)

class PostAdmin(admin.ModelAdmin):
    list_display = ['name','text','category', 'display_tags', 'has_image', 'clear_rating', 'is_active']
    actions = [clear_rating, set_active]


admin.site.register(Post, PostAdmin)


class TagAdmin(admin.ModelAdmin):
    list_display = ['name','is_active']
    actions = [clear_rating, set_active]

admin.site.register(Tag, TagAdmin)