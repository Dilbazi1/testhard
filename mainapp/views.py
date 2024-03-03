from rest_framework.viewsets import ModelViewSet
from .models import Product, Group, UserCourse, Lesson
from .serializers import ProductModelSerializers, \
    GroupModelSerializers, UserCourseModelSerializers, \
    LessonModelSerializers


class ProductModelViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductModelSerializers


class GroupModelViewSet(ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupModelSerializers


class StudentModelViewSet(ModelViewSet):
    queryset = UserCourse.objects.all()
    serializer_class = UserCourseModelSerializers


class LessonModelViewSet(ModelViewSet):
    queryset = Lesson.objects.all()
    serializer_class = LessonModelSerializers
