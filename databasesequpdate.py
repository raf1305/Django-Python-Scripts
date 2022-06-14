from django.db import connection
import re

tables = ['ItemManagement_item','ItemManagement_itemcategory','ItemManagement_brand','ItemManagement_productmeta']
query_string = """
select setval('inventory."TABLE_NAME_id_seq"',(select max(id) from inventory."TABLE_NAME"));
"""
query_string_main = ''
for i in tables:
    query_string_main = query_string_main + re.sub('TABLE_NAME',i,query_string)

schema="inventory"
with connection.cursor() as cursor:
    cursor.execute(f"SET search_path to {schema}")
    cursor.execute(query_string_main)

# with connection.cursor() as cursor:
#     cursor.execute(f"CREATE SCHEMA IF NOT EXISTS {schema}")
#     cursor.execute(f"SET search_path to {schema}")
# str = 'SELECT setval(\'asiflikk77."Barcode_barcodeitem_id_seq"\', (SELECT MAX(id) FROM asiflikk77."Barcode_barcodeitem"));'
#     str = str + 'SELECT setval(\'asiflikk77."Barcode_barcodeinfo_id_seq"\', (SELECT MAX(id) FROM asiflikk77."Barcode_barcodeinfo"));'
#     str = str + 'SELECT setval(\'asiflikk77."Customer_customer_id_seq"\', (SELECT MAX(id) FROM asiflikk77."Customer_customer"));'
#     str = str + 'select setval(\'asiflikk77."ItemManagement_itemcategory_id_seq"\', (SELECT MAX(id) FROM asiflikk77."ItemManagement_itemcategory"));'
#     str = str + 'SELECT setval(\'asiflikk77."ItemManagement_item_id_seq"\', (SELECT MAX(id) FROM asiflikk77."ItemManagement_item"));'
#     str = str + 'SELECT setval(\'asiflikk77."Material_stockitem_id_seq"\', (SELECT MAX(id) FROM asiflikk77."Material_stockitem"));'
#     str = str + 'SELECT setval(\'asiflikk77."Supplier_supplier_id_seq"\', (SELECT MAX(id) FROM asiflikk77."Supplier_supplier"));'
#     str = str + 'SELECT setval(\'asiflikk77."Supplier_contactperson_id_seq"\', (SELECT MAX(id) FROM asiflikk77."Supplier_contactperson"));'
#     str = str + 'SELECT setval(\'asiflikk77."ItemManagement_productmeta_id_seq"\', (SELECT MAX(id) FROM asiflikk77."ItemManagement_productmeta"));'
#     cursor.execute(str)