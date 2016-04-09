from django.contrib import admin
from Blog.models import Article, Category, Tag


class ArticleAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'category', 'status', 'pub_date')
    list_display_links = ('title',)
    search_fields = ['title', 'slug', 'pub_date', 'modified', 'category', 'tags']
    list_filter = ['pub_date', 'status', 'category']
    date_hierarchy = 'pub_date'


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Article, ArticleAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
