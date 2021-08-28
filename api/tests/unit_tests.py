from api.views import ProjectViewSet
from django.test import TestCase
from rest_framework.test import APIClient
from unittest.mock import patch
from rest_framework import status

from api.serializers import ProjectSerializer
from api.tests.mocks import MockPypiResponse
from api.models import PackageRelease, Project


class UnitTestsSerializers(TestCase):

    def setUp(self):
        self.client = APIClient()
        Project.objects.create(name="titan")

    @patch("api.request.PypiResponse", return_value=MockPypiResponse())
    def test_get_package_with_version_if_param_dont_has_version(self, mocked):
        package = {"name": "Django"}
        expect = {"name": "Django", "version": "3.2.6"}
        self.assertEqual(
            ProjectSerializer.get_package_with_version(package), expect)

    @patch("api.request.PypiResponse", return_value=MockPypiResponse())
    def test_get_package_with_version_if_param_has_version(self, mocked):
        package = {"name": "Django", "version": "3.2.5"}
        expect = {"name": "Django", "version": "3.2.5"}
        self.assertEqual(
            ProjectSerializer.get_package_with_version(package), expect)

    @patch("api.request.PypiResponse", return_value=MockPypiResponse())
    def test_create_packages(self, mocked):
        packages = [{"name": "Django"}, {"name": "graphene", "version": "2.0"}]
        project = Project.objects.get(name="titan")

        self.assertEqual(project.name, "titan")
        self.assertEqual(str(project), "titan")

        ProjectSerializer.create_packages(packages, project)

        inserted_packages = PackageRelease.objects.all()

        self.assertEqual(inserted_packages[0].name, "Django")
        self.assertEqual(inserted_packages[0].version, "3.2.6")
        self.assertEqual(str(inserted_packages[0]), "Django 3.2.6")
        self.assertEqual(inserted_packages[1].name, "graphene")
        self.assertEqual(inserted_packages[1].version, "2.0")
        self.assertEqual(str(inserted_packages[1]), "graphene 2.0")

    @patch("api.request.PypiResponse", return_value=MockPypiResponse())
    def test_create_project(self, mocked):
        project = {
            "name": "titan2",
            "packages": [
                {"name": "Django"},
                {"name": "graphene", "version": "2.0"}
            ]
        }

        ProjectSerializer.create(self, project)
        project = Project.objects.get(name="titan2")
        inserted_packages = PackageRelease.objects.all()

        self.assertEqual(project.name, "titan2")
        self.assertEqual(inserted_packages[0].name, "Django")
        self.assertEqual(inserted_packages[0].version, "3.2.6")
        self.assertEqual(inserted_packages[1].name, "graphene")
        self.assertEqual(inserted_packages[1].version, "2.0")

class UnitTestsViews(TestCase):

    def test_appropriate_response_if_serializer_is_not_valid(self):
        serializer = ProjectSerializer(data={
        "packages": [
            {"name": "Django", "version": "3.2.6"},
        ]})

        response = ProjectViewSet.appropriate_response(serializer)
       
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

