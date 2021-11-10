from django.contrib import admin
from .models import ReviewModel

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_name', 'user', 'bet', 'created', 'updated')
    list_editable = ('user_name', 'user', 'bet')
    search_fields = ('id', 'user_name', 'user', 'bet', 'created', 'updated')
    ordering = ('-updated', '-created')
    list_filter = ('user_name', 'user', 'created', 'updated')

admin.site.register(ReviewModel, PostAdmin)