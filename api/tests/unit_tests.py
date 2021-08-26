from django.test import TestCase
from rest_framework.test import APIClient
from unittest.mock import patch

from api.serializers import ProjectSerializer
from api.tests.mocks import MockPypiResponse
from api.models import PackageRelease, Project

class UnitTestsSerializers(TestCase):

    def setUp(self):
        self.client = APIClient()
        Project.objects.create(name="titan")
       

    @patch("magpy.request.PypiResponse", return_value=MockPypiResponse())
    def test_get_package_with_version_if_param_dont_has_version (self, mocked):
        package = {"name": "Django"}
        expect = {"name": "Django", "version": "3.2.6" }
        self.assertEqual(ProjectSerializer.get_package_with_version(package), expect )


    @patch("magpy.request.PypiResponse", return_value=MockPypiResponse())
    def test_get_package_with_version_if_param_has_version (self, mocked):
        package = {"name": "Django", "version": "3.2.5"}
        expect = {"name": "Django", "version": "3.2.5" }
        self.assertEqual(ProjectSerializer.get_package_with_version(package), expect )
    

    @patch("magpy.request.PypiResponse", return_value=MockPypiResponse())
    def test_create_packages (self, mocked):
        packages = [{"name": "Django"}, {"name": "graphene", "version": "2.0"}]
        project = Project.objects.get(name="titan")

        self.assertEqual(project.name, "titan")

        ProjectSerializer.create_packages(packages, project)

        inserted_package = PackageRelease.objects.all()
        print(inserted_package)

        self.assertEqual(inserted_package[0].name, "Django")
        self.assertEqual(inserted_package[0].version, "3.2.6")
        self.assertEqual(inserted_package[1].name, "graphene")
        self.assertEqual(inserted_package[1].version, "2.0")

    @patch("magpy.request.PypiResponse", return_value=MockPypiResponse())
    def test_create_project (self, mocked):
        project = {
            "name": "titan2",
            "packages": [
                {"name": "Django"},
                {"name": "graphene", "version": "2.0"}
            ]
        }

        ProjectSerializer.create(self, project)
        project = Project.objects.get(name="titan2")
        inserted_package = PackageRelease.objects.all()

        self.assertEqual(project.name, "titan2")
        self.assertEqual(inserted_package[0].name, "Django")
        self.assertEqual(inserted_package[0].version, "3.2.6")
        self.assertEqual(inserted_package[1].name, "graphene")
        self.assertEqual(inserted_package[1].version, "2.0")
