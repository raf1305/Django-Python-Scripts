import re

from django.core.management.commands.migrate import Command as MigrationCommand

from django.db import connection

from Company.models import Company
from ...utils import get_tenants_list


class Command(MigrationCommand):
    def handle(self, *args, **options):
        schemas = get_tenants_list()

        with connection.cursor() as cursor:
            for schema in schemas:
                print(schema)
                cursor.execute(f"CREATE SCHEMA IF NOT EXISTS {schema}")
                cursor.execute(f"SET search_path to {schema}")
                # '''
                # Drop migration records
                # '''
                try:
                    sss = '''
                    DELETE FROM schema.django_migrations where app='Ecom';
                    '''
                    sss = re.sub('schema', schema, sss)
                    print(sss)
                    cursor.execute(sss)

                except Exception as e:
                    print(repr(e))
                    pass
