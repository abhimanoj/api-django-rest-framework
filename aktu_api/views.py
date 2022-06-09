from rest_framework import viewsets
from .models import *
from .serializers import *
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter, SearchFilter

class UniversityClassView(viewsets.ModelViewSet):
    serializer_class = UniversitySerializer
    queryset = University.objects.all()


class CoursesClassView(viewsets.ModelViewSet):
    serializer_class = CoursesSerializer
    queryset = Courses.objects.all()


class SyllabusesClassView(viewsets.ModelViewSet):
    serializer_class = SyllabusesSerializer
    queryset = Syllabuses.objects.all()


class UserTableClassView(viewsets.ModelViewSet):
    serializer_class = UserTableSerializer
    queryset = UserTable.objects.all()

    # Apply Filter..
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)

    filterset_fields = ("enrollment", "syllabuse", "syllabuse__cource")
    # Apply Sorting..
    ordering_fields = ["created_at"]
    # Serchalble Fields..
    search_fields = ["name"]





