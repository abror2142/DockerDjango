from django.contrib import admin
from .models import Follower, Message
# Register your models here.


@admin.register(Follower)
class FollowerAdmin(admin.ModelAdmin):
    list_display = ['id', 'follower', 'user']
    list_display_links = ['id']


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ['id', 'from_user', 'to_user', 'content']
    list_display_links = ['id']