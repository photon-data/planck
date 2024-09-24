from rest_framework import status
from django.contrib.auth import get_user_model

from rest_framework.test import APITestCase
from ..models import VersionControl, VersionControlType
from django.test.utils import override_settings
from django.conf import settings

class VersionControlAPITest(APITestCase):
    def setUp(self):
        User = get_user_model()
        self.user = User.objects.create_user(
            username='testuser',
            password='testpassword'
        )

        self.type = VersionControlType.objects.create(name='gitlab')
        self.url = '/api/v1/connection/versioncontrol/'
        self.client.force_authenticate(user=self.user)


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
