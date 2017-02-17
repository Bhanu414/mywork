from django.contrib import admin

# Register your models here.
from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ["Title", "Timestamp", "Updated"]
    list_display_links = ["Updated"]
    list_filter = ["Title"]
    search_fields = ["Content"]
    class Meta:
        model = Post

admin.site.register(Post ,PostAdmin)