from rest_framework import serializers 
from .models import Student, University 

class UniversitySerializer(serializers.ModelSerializer):
    class Meta:
        model = University
        fields = ['id', 'name', 'location']
 
class StudentSerializer(serializers.ModelSerializer): 
    university = UniversitySerializer(read_only=True)
    university_id = serializers.PrimaryKeyRelatedField(
        queryset=University.objects.all(),
        source='university',
        write_only=True
    )
    class Meta: 
        model = Student 
        fields = ['id', 'first_name', 'last_name', 'email', 'university', 'university_id'] 
