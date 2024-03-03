from django.contrib import admin
from .models import Product,Group,Lesson,UserCourse
admin.site.register(Product)
admin.site.register(Lesson)
admin.site.register(Group)
admin.site.register(UserCourse)

