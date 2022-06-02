from django.contrib import admin
from .models import User,tags

# Register your models here.

class UserAdmin(admin.ModelAdmin):
    filter_horizontal =('tags',)


admin.site.register(User)
admin.site.register(tags)
