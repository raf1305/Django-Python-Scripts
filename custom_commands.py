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
                    DELETE FROM schema.django_migrations where app='Ecom' and name != '0001_initial';
                    '''
                    sss = re.sub('schema', schema, sss)
                    print(sss)
                    cursor.execute(sss)

                except Exception as e:
                    print(repr(e))
                    pass

                # '''
                # Drop specific tables
                # '''
                # # ss = 'DROP TABLE if exists "Company_company","Company_schemainfo","Company_companyconfiguration" cascade'
                # s = ['Ecom_ecomitemimage', 'Ecom_ecomitemmeta', 'Ecom_ecomitemtags', 'Ecom_ecomitemattribute'
                #      , 'Ecom_ecomitem', 'Ecom_ecombrandtags', 'Ecom_ecombrand', 'Ecom_ecomcategorytags', 'Ecom_ecomcategory'
                #      ]
                # for i in s:
                #     ss = f'DELETE FROM "{i}"'
                #     cursor.execute(ss)
