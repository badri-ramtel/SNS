from django.contrib import admin
from gallery_app.models import Category, Photo

# Register your models here.
admin.site.register(Category)
admin.site.register(Photo)