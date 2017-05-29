from django.contrib import admin
from models import *


# Register your models here.
class FishPhotoAdmin(admin.ModelAdmin):
    list_display = ('createdAt', 'photo')


admin.site.register(FishPhoto, FishPhotoAdmin)
