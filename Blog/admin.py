# -*- encoding:utf-8 -*-
from django.contrib import admin
from django import forms
from Blog.models import Article, Category, Tag
from tinymce.widgets import TinyMCE


class ArticleAdminForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = '__all__'
        widgets = {
            'text': TinyMCE(),
        }


class ArticleAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'category', 'status', 'pub_date', 'was_published_recently')
    list_display_links = ('title',)
    search_fields = ['title', 'slug', 'pub_date', 'modified', 'category', 'tags']
    list_filter = ['pub_date', 'status', 'category']
    date_hierarchy = 'pub_date'
    readonly_fields = ('pub_date', 'modified')
    fieldsets = [
        ('Публикация', {'fields': [('title', 'slug')]}
         ),
        ('Содержимое', {'fields': [('category', 'text')]}
         ),
        ('Дата публикации', {'fields': [('pub_date', 'modified')]}
         ),
        ('Теги', {'fields': ['tags'], 'classes': ['collapse']}
         ),
        ('Статус', {'fields': ['status']}
         ),
    ]
    form = ArticleAdminForm

    def make_published(self, request, queryset):
        queryset.update(status='P')
    make_published.short_description = 'Пометить как опубликованное'

    def make_draft(self, request, queryset):
        queryset.update(status='D')
    make_draft.short_description = 'Пометить как черновик'

    def make_expired(self, request, queryset):
        updated = queryset.update(status='E')
        if (updated == 1):
            massage_b = '1 запись была'
        else:
            massage_b = '%s записей были' %updated
        self.message_user(request, '%s, успешно помечено как устаревшие' %massage_b)

    actions = ['make_published', 'make_draft', 'make_expired']


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Article, ArticleAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
