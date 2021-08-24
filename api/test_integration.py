from magpy.request import PypiResponse
import api
from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status

from api.models import Project




class ProjectsApiTests(TestCase):

    def setUp(self):
        self.client = APIClient()


    def test_create_project_were_packages_have_correct_versions_and_names(self):
        project = {
            "name": "titan",
            "packages": [
                {"name": "Django", "version": "3.2.5"},
                {"name": "graphene", "version": "2.0"}]}


        response = self.client.post('/api/projects/', data=project, format='json')

        exists = Project.objects.filter(
            name = project["name"]
        ).exists()

        self.assertTrue(exists)
        self.assertDictEqual(response.data, project)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


    def test_create_project_with_incorrect_packages(self):
        project_with_incorrect_package_name = {
            "name": "titan",
            "packages": [
                {"name": "Djjango", "version": "3.2.5"},
                {"name": "graphene", "version": "2.0"}]}
        project_with_incorrect_package_version = {
            "name": "titan",
            "packages": [
                {"name": "Django", "version": "3.2.5"},
                {"name": "graphene", "version": "200"}]} 

        projects = [
            project_with_incorrect_package_name,
            project_with_incorrect_package_version
        ]

        for project in projects:
            response = self.client.post('/api/projects/', data=project, format='json')

            exists = Project.objects.filter(
                name = project["name"]).exists()

            self.assertFalse(exists)
            self.assertDictEqual(response.data, {"error": "One or more packages doesn't exist"})
            self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


    def test_create_project_without_package_version(self):
        project_without_package_version = {
            "name": "titan",
            "packages": [
                {"name": "Django"},
                {"name": "graphene"}]}

        response = self.client.post(
            '/api/projects/',
            data=project_without_package_version,
            format='json')

        exists = Project.objects.filter(
            name = project_without_package_version["name"]).exists()

        self.assertTrue(exists)
        for package in response.data["packages"]:
            self.assertIn("version", package)
            self.assertIsNot(package["version"], '')

       
    def test_find_project_by_name(self):

        project =  {
            "name": "titan",
            "packages": [
                {"name": "Django", "version": "3.2.6"},
                {"name": "graphene", "version": "2.1.9"}]}

        self.client.post(
            '/api/projects/',
            data=project, format='json')

        response = self.client.get('/api/projects/titan/')

        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_find_nonexistent_project(self):
        response = self.client.get('/api/projects/titan/')

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


    def test_delete_project_by_name(self):

        project =  {
            "name": "titan",
            "packages": [
                {"name": "Django", "version": "3.2.6"},
                {"name": "graphene", "version": "2.1.9"}]}

        self.client.post(
            '/api/projects/',
            data=project, format='json')

        exists_before_deletion = Project.objects.filter(
            name = project["name"]).exists()

        self.assertTrue(exists_before_deletion)

        response = self.client.delete('/api/projects/titan/')

        exists_after_deletion = Project.objects.filter(
            name = project["name"]).exists()

        self.assertFalse(exists_after_deletion)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


    def test_delete_nonexistent_project_by_name(self):

        response = self.client.delete('/api/projects/titan/')

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
