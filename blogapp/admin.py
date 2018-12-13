from django.contrib import admin
from blogapp.models import Post,comments

# Register your models here.

admin.site.register(Post)
admin.site.register(comments)