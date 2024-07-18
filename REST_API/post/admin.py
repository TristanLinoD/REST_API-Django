from django.contrib import admin
from .models import Post

# Register your models here.
class PostAdmin(admin.ModelAdmin):
  list_display = ('title', 'description')  # Columns to display in the list view
  # We can add diffent things if we needed it for example we can filter on publish date in case we have that field
  # search_fields = ('title', 'content')  # Fields to search within the admin
  # list_filter = ('publish_date', 'author')  # Filters to apply in the list view
  # ordering = ('-publish_date',)  # Default ordering of the list view
  # fields = ('title', 'content', 'author', 'publish_date')  # Fields to include in the edit form

admin.site.register(Post, PostAdmin)
