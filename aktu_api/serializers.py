from rest_framework import serializers
from .models import *
 

class UniversitySerializer(serializers.ModelSerializer):   
 
    class Meta:
        model = University
        fields = ('__all__')
 
class CoursesSerializer(serializers.ModelSerializer):   

    class Meta:
        model = Courses
        fields = ('__all__')
 
class SyllabusesSerializer(serializers.ModelSerializer):   

    class Meta:
        model = Syllabuses
        fields = ('__all__')
 
class UserTableSerializer(serializers.ModelSerializer):   

    class Meta:
        model = UserTable
        fields = ('__all__')
 