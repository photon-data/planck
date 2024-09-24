from rest_framework import status
from rest_framework.test import APITestCase
from ..models import VersionControl, VersionControlType

class VersionControlAPITest(APITestCase):
    def setUp(self):
        self.type = VersionControlType.objects.create(name='gitlab')
        self.url = '/api/v1/connection/versioncontrol/'

    def test_create_version_control(self):
        data = {
            'connection_name': 'my_gitlab_connection',
            'type': 'gitlab',
            'data': {
                'api_token': 'token123',
                'username': 'user1',
                'project_id': 'testid'
            }
        }
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(VersionControl.objects.count(), 1)
        self.assertEqual(VersionControl.objects.get().connection_name, 'my_gitlab_connection')

    def test_create_version_control_unique_name(self):
        data = {
            'connection_name': 'my_gitlab_connection',
            'type': 'gitlab',
            'data': {
                'api_token': 'token123',
                'username': 'user1',
                'project_id':'testid'
            }
        }
        self.client.post(self.url, data, format='json')  # Create first instance
        response = self.client.post(self.url, data, format='json')  # Attempt to create duplicate
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('connection_name', response.data)

    def test_list_version_controls(self):
        VersionControl.objects.create(
            connection_name='my_gitlab_connection',
            type=self.type,
            data={'api_token': 'token123', 'username': 'user1'}
        )
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
