from django.contrib import admin
from featured_book.models import featured_book

class FeaturedBookAdmin(admin.ModelAdmin):
    list_display = ('book_name', 'book_author', 'book_price')
    
admin.site.register(featured_book, FeaturedBookAdmin)


