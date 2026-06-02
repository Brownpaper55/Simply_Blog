from django.contrib import admin

from Accounts.models import CustomUser
from Blog.models import Post

# Register your models here.
admin.site.register(CustomUser)
admin.site.register(Post)
