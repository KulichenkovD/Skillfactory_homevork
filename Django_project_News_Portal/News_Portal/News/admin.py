from django.contrib import admin
from .models import *

# admin.site.unregister()
admin.site.register(Author)
admin.site.register(Post)
admin.site.register(PostCategory)
admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(New)