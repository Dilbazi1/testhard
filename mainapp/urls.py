from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import ProductModelViewSet, GroupModelViewSet,StudentModelViewSet,LessonModelViewSet

app_name = 'mainapp'

router = DefaultRouter()

router.register('groups', GroupModelViewSet)
router.register('products', ProductModelViewSet)
router.register('students', StudentModelViewSet)
router.register('lesson', LessonModelViewSet)

urlpatterns = [
    path('', include(router.urls))
]
