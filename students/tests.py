from django.test import TestCase
from .models import University, Student

class UniversityModelTest(TestCase):

    def test_create_university(self):
        uni = University.objects.create(
            name="MIT",
            location="Cambridge"
        )
        self.assertEqual(University.objects.count(), 1)
        self.assertEqual(str(uni), "MIT")


class StudentModelTest(TestCase):

    def test_create_student(self):
        uni = University.objects.create(name="Oxford", location="UK")

        student = Student.objects.create(
            first_name="John",
            last_name="Doe",
            email="john@example.com",
            university=uni
        )

        self.assertEqual(Student.objects.count(), 1)
        self.assertEqual(str(student), "John Doe")
        self.assertEqual(student.university.name, "Oxford")


from rest_framework.test import APIClient
from django.urls import reverse

class UniversityApiTest(TestCase):

    def setUp(self):
        self.client = APIClient()

    def test_add_university(self):
        url = reverse("add_university")
        payload = {
            "name": "Harvard",
            "location": "USA"
        }

        response = self.client.post(url, payload, format='json')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(University.objects.count(), 1)


class StudentApiTest(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.uni = University.objects.create(name="Stanford", location="USA")

    def test_add_student(self):
        url = reverse("add_student")

        payload = {
            "first_name": "Alice",
            "last_name": "Smith",
            "email": "alice@example.com",
            "university_id": self.uni.id
        }

        response = self.client.post(url, payload, format='json')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(Student.objects.count(), 1)
        self.assertEqual(Student.objects.first().university.name, "Stanford")

    def test_get_all_students(self):
        Student.objects.create(
            first_name="Bob",
            last_name="Marley",
            email="bob@example.com",
            university=self.uni
        )

        url = reverse("get_all_students")
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)

    def test_update_student(self):
        student = Student.objects.create(
            first_name="Tom",
            last_name="Jerry",
            email="tj@example.com",
            university=self.uni
        )

        url = reverse("update_student", args=[student.id])

        data = {"first_name": "Tommy"}

        response = self.client.put(url, data, format='json')

        self.assertEqual(response.status_code, 200)
        student.refresh_from_db()
        self.assertEqual(student.first_name, "Tommy")
    def test_delete_student(self):
        student = Student.objects.create(
            first_name="Max",
            last_name="Payne",
            email="max@example.com",
            university=self.uni
        )

        url = reverse("delete_student", args=[student.id])
        response = self.client.delete(url)

        self.assertEqual(response.status_code, 204)
        self.assertEqual(Student.objects.count(), 0)

    def test_search_students(self):
        Student.objects.create(
            first_name="Karim",
            last_name="Benzema",
            email="kb9@example.com",
            university=self.uni
        )

        url = reverse("search_students") + "?q=Kar"
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["first_name"], "Karim")
