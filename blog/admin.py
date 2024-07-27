from django.contrib import admin
from . models import Tag, Comment, Blog, Categories, Newsletter

 
admin.site.register(Blog)
admin.site.register(Newsletter)
admin.site.register(Tag)
admin.site.register(Comment)
admin.site.register(Categories)
