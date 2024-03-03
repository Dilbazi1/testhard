from rest_framework.serializers import ModelSerializer
from .models import Product, Group, UserCourse, Lesson
from rest_framework import serializers
from django_filters import rest_framework as filters


class ProductModelSerializers(ModelSerializer):
    lessons_count = serializers.SerializerMethodField()
    usercourse_count = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = '__all__'

    def get_lessons_count(self, obj):
        return obj.lesson_set.count()

    def get_usercourse_count(self, obj):
        return obj.usercourse_set.count()


class GroupModelSerializers(ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'


class UserCourseModelSerializers(ModelSerializer):
    class Meta:
        model = UserCourse
        fields = '__all__'


class LessonModelSerializers(ModelSerializer):
    # product=ProductModelSerializers()
    class Meta:
        model = Lesson
        fields = ['product', 'name', 'link', ]
