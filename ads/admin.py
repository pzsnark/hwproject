from django.contrib import admin
from .models import Profile, Ad, Category, Comment, Message

# Register your models here.
admin.site.register(Profile)
admin.site.register(Ad)
admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(Message)
