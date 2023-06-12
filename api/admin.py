from django.contrib import admin
from django.utils.html import format_html
from . import models

def dublicate_ad(modeladmin, request, queryset):
    # клонирование выбранных Ad
    for el in queryset:
        el.pk = None
        el.save()


dublicate_ad.short_description = "Дублировать объект"

admin.site.register(models.FeedbackText)
admin.site.register(models.Questions)
admin.site.register(models.Service)

@admin.register(models.Illustration)
class IllustrationAdmin(admin.ModelAdmin):
    list_display = ('title', 'count', 'image_tag', 'id')
    list_editable = ['count']
    actions = [dublicate_ad]

    def image_tag(self, obj):
        return format_html(f'<img width="100" src="{obj.img.url}" />')

    image_tag.short_description = 'Изображение'

@admin.register(models.FeedbackVideo)
class FeedbackVideoAdmin(admin.ModelAdmin):
    list_display = ('name', 'created', 'video_tag')
    actions = [dublicate_ad]

    def name(self, obj):
        return f'Видео отзыв - №{obj.id}'

    def video_tag(self, obj):
        return format_html(f'<video width="100" src="{obj.video.url}" muted autoplay loop />')

    video_tag.short_description = 'Видео'
    name.short_description = 'Название'