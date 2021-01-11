from django.utils import timezone
import datetime
from django.contrib import admin
from django.contrib.admin import StackedInline
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .forms import AdminFormAd, AudioForm

from .models import Profile, Ad, Category, Comment, Message, Audio

admin.site.unregister(User)

admin.site.register(Profile)
admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(Message)
admin.site.register(Audio)


class CommentInline(StackedInline):
    model = Comment
    extra = 1
    max_num = 5
    fields = ['author', 'text']


def delete_old_posts(queryset):
    queryset.filter(date_pub__lte=timezone.now() - datetime.timedelta(weeks=2)).delete()


@admin.register(Ad)
class AdAdmin(admin.ModelAdmin):
    # fields = ['author', 'title', 'description', 'date_pub', 'date_up', 'favorite', 'categories']
    readonly_fields = ['date_pub', 'date_up']
    fieldsets = [
        ('Основные поля', {
            'fields': ['author', 'title', 'description', 'photo', 'favorite', 'categories']
        }),
        ('Даты/время', {
            'fields': [
                'date_pub',
                'date_up'
            ]
        })

    ]
    inlines = [CommentInline]
    list_display = ('author', 'title', 'date_pub')
    actions = [delete_old_posts]
    form = AdminFormAd


class ProfileInline(StackedInline):
    model = Profile


@admin.register(User)
class UserAdmin(UserAdmin):
    inlines = [ProfileInline]


class AdminAudio(admin.ModelAdmin):
    model = Audio
    form = AudioForm
