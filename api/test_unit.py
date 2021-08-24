from magpy.request import PypiResponse
import api
from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status

from api.models import Project




class UnitTests(TestCase):

    def setUp(self):
        self.client = APIClient()


    


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
        
