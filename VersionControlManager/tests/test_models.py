from django.test import TestCase
from ..models import VersionControl, VersionControlType

class VersionControlTypeModelTest(TestCase):
    def setUp(self):
        self.type = VersionControlType.objects.create(name='GitLab')

    def test_version_control_type_str(self):
        self.assertEqual(str(self.type), 'GitLab')


class VersionControlModelTest(TestCase):
    def setUp(self):
        self.type = VersionControlType.objects.create(name='GitLab')
        self.version_control = VersionControl.objects.create(
            connection_name='my_gitlab_connection',
            type=self.type,
            data={'api_token': 'token123', 'username': 'user1'}
        )

    def test_version_control_str(self):
        self.assertEqual(str(self.version_control), 'my_gitlab_connection (GitLab)')

    def test_unique_connection_name(self):
        with self.assertRaises(Exception):  # Expecting IntegrityError
            VersionControl.objects.create(
                connection_name='my_gitlab_connection',
                type=self.type,
                data={'api_token': 'token456', 'username': 'user2'}
            )
