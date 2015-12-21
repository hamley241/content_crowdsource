from django.contrib import admin

# Register your models here.
from tagsource.models import Sticker, Tag




class TagInline(admin.TabularInline):
    model = Tag
    list_display = ['name']
    extra = 3

class StickerAdmin(admin.ModelAdmin):
    # fields = ['name','category']
    inlines = [TagInline]
    fieldsets = [
        (None, {'fields':['name','category']}),
        # ('Tags',{'inlines':['inlines']})
    ]
admin.site.register(Sticker,StickerAdmin)
