from rest_framework.decorators import api_view 
from rest_framework.response import Response 
from rest_framework import status
from django.db.models import Q
from .models import Student, University
from .serializers import StudentSerializer, UniversitySerializer
 

 # ---------- university ----------
@api_view(['POST'])
def add_university(request):
    serializer = UniversitySerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"message": "University added successfully"})
    return Response(serializer.errors, status=400)

@api_view(['GET'])
def get_all_universities(request):
    universities = University.objects.all()
    serializer = UniversitySerializer(universities, many=True)
    return Response(serializer.data)


# ---------- Student ----------
@api_view(['POST']) 
def add_student(request): 
    serializer = StudentSerializer(data=request.data) 
    if serializer.is_valid(): 
        serializer.save() 
        return Response({"message": "New student is added"}) 
    return Response(serializer.errors, status=400) 
 
@api_view(['GET']) 
def get_all_students(request): 
    students = Student.objects.all() 
    serializer = StudentSerializer(students, many=True) 
    return Response(serializer.data) 

@api_view(['PUT'])
def update_student(request, id):
    try:
        student = Student.objects.get(id=id)
    except Student.DoesNotExist:
        return Response({"error": "Student not found"}, status=status.HTTP_404_NOT_FOUND)

    serializer = StudentSerializer(student, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response({"message": "Student updated successfully"})
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_student(request, id):
    try:
        student = Student.objects.get(id=id)
    except Student.DoesNotExist:
        return Response({"error": "Student not found"}, status=status.HTTP_404_NOT_FOUND)

    student.delete()
    return Response({"message": "Student deleted successfully"}, status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
def search_students(request):
    query = request.GET.get('q', '')
    students = Student.objects.filter(
        Q(first_name__icontains=query) |
        Q(last_name__icontains=query) |
        Q(email__icontains=query) |
        Q(university__name__icontains=query)
    )
    serializer = StudentSerializer(students, many=True)
    return Response(serializer.data)