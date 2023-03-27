from django.contrib import admin
from django.db.models.base import Model

from .models import *

# Register your models here.


admin.site.register(User)

class MessageInline(admin.TabularInline):
    model = Message


class RoomAdmin(admin.ModelAdmin):
    list_display = ('name', 'topic', 'host')
    inlines = [MessageInline]    

admin.site.register(Room, RoomAdmin)


class RoomInline(admin.TabularInline):
    model = Room


class TopicAdmin(admin.ModelAdmin):
    inlines = [RoomInline]

admin.site.register(Topic, TopicAdmin)
admin.site.register(Message)

