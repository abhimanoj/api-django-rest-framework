from django.urls import path
from . import views
from django.urls import include

from rest_framework import routers

router = routers.DefaultRouter()

router.register(r'university', views.UniversityClassView, 'university')
router.register(r'courses', views.CoursesClassView, 'courses')
router.register(r'syllabuses', views.SyllabusesClassView, 'syllabuses')
router.register(r'user-table', views.UserTableClassView, 'user-table')
 
urlpatterns = [
    path('api-', include(router.urls)),
]