from django.contrib import admin
from .models import Student, Category, Subcategory,Landing,VideoBanner,Logo
# Register your models here.
admin.site.register(Student)
admin.site.register(Category)
admin.site.register(Subcategory)
admin.site.register(Landing)
admin.site.register(Logo)
admin.site.register(VideoBanner)
