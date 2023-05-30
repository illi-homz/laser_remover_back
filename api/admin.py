from django.contrib import admin
from django.utils.html import format_html
from .models import Any, Banner  # add this

admin.site.register(Any) # add this

def dublicate_ad(modeladmin, request, queryset):
    # клонирование выбранных Ad
    for el in queryset:
        el.pk = None
        el.save()


dublicate_ad.short_description = "Дублировать объект"

@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ('title', 'img', 'image_tag')
    list_editable = ['img']
    actions = [dublicate_ad]

    def image_tag(self, obj):
        return format_html('<img width="100" src="{}" />'.format(obj.img.url))

    image_tag.short_description = 'Картинка'