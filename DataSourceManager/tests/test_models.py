from django.test import TestCase
from ..models import DataSourceType, DataSource

class DataSourceTypeModelTest(TestCase):
    def setUp(self):
        self.ds_type = DataSourceType.objects.create(name='postgres1',required_fields=["host", "port", "user", "password", "database"])

    def test_data_source_type_str(self):
        self.assertEqual(str(self.ds_type), 'postgres1')


    def test_data_source_type_required_fields(self):
        self.assertEqual(self.ds_type.required_fields,["host", "port", "user", "password", "database"])




class DataSourceModelTest(TestCase):
    def setUp(self):
        self.ds_type = DataSourceType.objects.create(name='postgres1',required_fields=["host", "port", "user", "password", "database"])
        self.data_source = DataSource.objects.create(
            connection_name='postgres_test_connection',
            type=self.ds_type,
            data={'host': '127.0.0.1',
                  'port': '5432',
                  'user':'kabzadebig',
                  'password':'verstrongpassword',
                  'database':'test_db'
                  }
        )

    def test_data_source_str(self):
        self.assertEqual(str(self.data_source), 'postgres_test_connection (postgres1)')

    def test_unique_connection_name(self):
        with self.assertRaises(Exception):  # Expecting IntegrityError
             DataSource.objects.create(
                connection_name='postgres_test_connection',
                type=self.ds_type,
                data={'host': '127.0.0.1',
                      'port': '5432',
                      'user': 'kabzadebig',
                      'password': 'verstrongpassword',
                      'database': 'test_db'
                      }
            )