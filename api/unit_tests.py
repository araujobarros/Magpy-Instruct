from api.serializers import PackageSerializer, ProjectSerializer
from magpy.request import PypiResponse

from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from unittest.mock import patch

from api.models import Project

class MockResponse:
 
    def __init__(self):
        self.status_code = 200
 
    def json(self):
        return {
            "info": {
                "version": "3.2.6"
            }
        }


class UnitTestsSerializers(TestCase):

    def setUp(self):
        self.client = APIClient()

    @patch("requests.get", return_value=MockResponse())
    def test_get_package_with_version_if_param_dont_has_version (self, mocked):
        package = {"name": "Django"}
        expect = {"name": "Django", "version": "3.2.6" }
       

        self.assertEqual(ProjectSerializer.get_package_with_version(package), expect )
    


    # def test_create_project_without_package_version(self, mock_request_packages_by_pypi):
    #     project_without_package_version = {
    #         "name": "titan",
    #         "packages": [
    #             {"name": "Django"},
    #             {"name": "graphene"}]}

    #     response = self.client.post(
    #         '/api/projects/',
    #         data=project_without_package_version,
    #         format='json')

    #     exists = Project.objects.filter(
    #         name = project_without_package_version["name"]).exists()

    #     self.assertTrue(exists)
    #     for package in response.data["packages"]:
    #         self.assertIn("version", package)
    #         self.assertIsNot(package["version"], '')

    #     pypi_response_1 = Mock(speck=PypiResponse)
    #     pypi_response_1.name = "Django"
    #     pypi_response_1.version = "3.2.6"

    #     pypi_response_2 = Mock(speck=PypiResponse)
    #     pypi_response_2.name = "graphene"
    #     pypi_response_2.version = "2.1.9"

    #     mock_request_packages_by_pypi.return_value = [pypi_response_1, pypi_response_2]
        
