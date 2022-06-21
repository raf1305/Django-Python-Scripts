import re

from django.core.management.commands.migrate import Command as MigrationCommand

from django.db import connection

from Company.models import Company
from ...utils import get_tenants_list


class Command(MigrationCommand):
    def handle(self, *args, **options):
        with connection.cursor() as cursor:
            ss = '''
                    SELECT table_name
                    FROM information_schema.columns
                    where table_name like 'Ecom%'
                 '''
            cursor.execute(ss)
            all_tables = set()
            for i in cursor.fetchall():
                all_tables.add(i[0])
            schemas = get_tenants_list()
            query_string = 'Drop table if exists '

            for schema in schemas:
                print(schema)
                cursor.execute(f"CREATE SCHEMA IF NOT EXISTS {schema}")
                cursor.execute(f"SET search_path to {schema}")
                for i in all_tables:
                    cursor.execute(query_string + f'"{i}" cascade')


