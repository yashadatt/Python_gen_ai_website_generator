from django.contrib import admin
from .models import WebsiteData,Author,Book,Review
# Register your models here.

admin.site.register(WebsiteData)
admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Review)
