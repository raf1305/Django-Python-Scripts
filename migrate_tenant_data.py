import csv
from django.db import connection

from ItemManagement.models import ItemCategory,Item,Unit,ProductMeta
from Customer.models import Customer,CreditLimit
from Supplier.models import Supplier,ContactPerson
from Material.models import StockItem
from Barcode.models import BarcodeInfo,BarcodeItem
from WearhouseStore.models import WearStore
from Shopbranchoutlet.models import SBO
from OldSystemManagement.models import OldPurchaseInfo,OldPurchaseDetails,OldSalesInfo,OldSalesDetails,OldStock,OldStockDetails

schema = "asiflikk77"
path = 'datamigration/amarpc_main_csv/'

categories = []
items = []
customers = []

with open(path+'category.csv',newline='',encoding="utf8") as cat:
    reader = csv.DictReader(cat)
    for row in reader:
        categories.append(ItemCategory(id=row['id'],
            category_name = row['category_name'],
            root=row['root'],
            level=row['level'],
            order=row['order'],
            # is_archived=row['is_archived'],
            # created_at=row['created_at'],
            parent_id=row['parent_id']))
        


with open(path+'item.csv',newline='',encoding="utf8") as cat:
    reader = csv.DictReader(cat)
    for row in reader:
        items.append(Item(id=row['id'],
                # code=row['code'],
                name=row['name'],
                quantity=row['quantity'],
                purchase_price=row['purchase_price'],
                sale_price=row['sale_price'],
                min_sale_price=row['min_sale_price'],
                vat=row['vat'],
                tax=row['tax'],
                # is_service=row['is_service'],
                # has_serial=row['has_serial'],
                # is_archived=row['is_archived'],
                # created_at=row['created_at'],
                category_id=row['category_id'],
                unit_id=row['unit_id']))

                
with open(path+'final_generated_customers.csv',newline='',encoding="utf8") as cat:
    reader = csv.DictReader(cat)
    for row in reader:
        customers.append(Customer(id=row['id'],
            name=row['name'],
            mobile=row['mobile'],
            email=row['email'],
            password=row['password'],
            apartment=row['apartment'],
            street_address=row['street_address'],
            city=row['city'],
            country=row['country'],
            cardno=row['cardno'],
            type=row['type'],
            # is_archived=row['is_archived'],
            # created_at=row['created_at'],
            info_id=row['info_id']))

credit_limit=[]
with open(path+'final_credit_limit.csv',newline='',encoding="utf8") as cat:
    reader = csv.DictReader(cat)
    for row in reader:
        credit_limit.append(CreditLimit(
            id=row['id'],
            value=row['value'],
            created_at=row['created_at'],
            created_by=row['created_by'],
            is_active=row['is_active'],
            customer_id=row['customer_id']
            ))

suppliers=[]
with open(path+'final_generated_suppliers.csv',newline='',encoding="utf8") as cat:
    reader = csv.DictReader(cat)
    for row in reader:
        suppliers.append(Supplier(id=row['id'], 
            name=row['name'],
            apartment=row['apartment'], 
            street_address=row['street_address'], 
            city=row['city'], 
            state=row['state'], 
            postal_code=row['postal_code'], 
            country=row['country'], 
            mobile_no=row['mobile_no'], 
            email_address=row['email_address'], 
            customer=row['customer'], 
            # is_archived=['is_archived'], 
            # created_at=row['created_at'],
            # assigned_user=0,
            credit_limit=row['credit_limit'],
            purchase_point=row['purchase_point'],
            restriction_level=row['restriction_level'],
            security_cheque_amount=row['security_cheque_amount'],
            security_cheque_number=row['security_cheque_number']
            ))

suppliers_contact_person=[]
with open(path+'final_generated_contact_person.csv',newline='',encoding="utf8") as cat:
    reader = csv.DictReader(cat)
    for row in reader:
        suppliers_contact_person.append(ContactPerson(
            id=row['id'], 
            name=row['name'],
            address=row['address'],
            mobile_no=row['mobile_no'],
            email_address=row['email_address'],
            is_archived=row['is_archived'], 
            created_at=row['created_at'], 
            supplier_id=row['supplier_id'],
            designation=row['designation']
        ))

# def find_keys(row):
#     keysList = list(row.keys())
#     return keysList

# def find_keys(reader):
#     for row in reader:
#         keysList = list(row.keys())
#         return keysList

# def config_object(keys,row,model):
#     m=model()
#     for i in range(len(keys)):
#         print(keys[i])
#         m.keys[i]=row[keys[i]]
#     print(m)

stockitems=[]
with open(path+'stockitem.csv',newline='',encoding="utf8") as cat:
    reader = csv.DictReader(cat)
    
    for row in reader:
        # print(type(row))
        # # data = config_object(keys,row,StockItem)
        # obj = namedtuple("StockItem",row.keys())(*row.values)
        # print(obj)
        # print(type(obj))
        # stockitems.append(StockItem(**row))
        # break
        stockitems.append(StockItem(
            id=row['id'],
            stockid=row['stockid'],
            total=row['total'],
            barcoded=row['barcoded'],
            finished=row['finished'],
            # expiry_date=row['expiry_date'],
            is_archived=row['is_archived'],
            created_at=row['created_at'],
            finished_at=row['finished_at'],
            chalanitem_id=row['chalanitem_id'],
            item_id=row['item_id'],
            store_id=row['store_id']
        ))
        
bcinfo=[]
with open(path+'bcinfo.csv',newline='',encoding="utf8") as cat:
    reader = csv.DictReader(cat)
    
    for row in reader:
        bcinfo.append(BarcodeInfo(**row))

bcitem=[]
with open(path+'bcitem.csv',newline='',encoding="utf8") as cat:
    reader = csv.DictReader(cat)
    
    for row in reader:
        bcitem.append(BarcodeItem(**row))

oldpurchaseinfo=[]
with open(path+'purchaseinfo.csv',newline='',encoding="utf8") as cat:
    reader = csv.DictReader(cat)
    for row in reader:
        oldpurchaseinfo.append(OldPurchaseInfo(**row))

oldpurchasedetails=[]
with open(path+'purchasedetails.csv',newline='',encoding="utf8") as cat:
    reader = csv.DictReader(cat)
    for row in reader:
        oldpurchasedetails.append(OldPurchaseDetails(**row))

oldsalesinfo=[]
with open(path+'salesinfo.csv',newline='',encoding="utf8") as cat:
    reader = csv.DictReader(cat)
    for row in reader:
        oldsalesinfo.append(OldSalesInfo(**row))

oldsalesdetails=[]
with open(path+'salesdetails.csv',newline='',encoding="utf8") as cat:
    reader = csv.DictReader(cat)
    for row in reader:
        oldsalesdetails.append(OldSalesDetails(**row))
itemmeta=[]
with open(path+'itemmeta.csv',newline='',encoding="utf8") as cat:
    reader = csv.DictReader(cat)
    for row in reader:
        itemmeta.append(ProductMeta(**row))


with connection.cursor() as cursor:
    cursor.execute(f"CREATE SCHEMA IF NOT EXISTS {schema}")
    cursor.execute(f"SET search_path to {schema}")
    ProductMeta.objects.all().delete()
    Item.objects.all().delete()
    Unit.objects.all().delete()
    ItemCategory.objects.all().delete()
    Customer.objects.all().delete()
    CreditLimit.objects.all().delete()
    Supplier.objects.all().delete()
    ContactPerson.objects.all().delete()
    BarcodeItem.objects.all().delete()
    BarcodeInfo.objects.all().delete()
    StockItem.objects.all().delete()
    OldPurchaseDetails.objects.all().delete()
    OldPurchaseInfo.objects.all().delete()
    OldSalesDetails.objects.all().delete()
    OldSalesInfo.objects.all().delete()
    # SBO.objects.all().delete()
    # WearStore.objects.all().delete()
    ItemCategory.objects.bulk_create(categories)
    Unit.objects.create(id=1,unit_name='piece')
    Item.objects.bulk_create(items)
    ProductMeta.objects.bulk_create(itemmeta)
    Customer.objects.bulk_create(customers)
    CreditLimit.objects.bulk_create(credit_limit)
    Supplier.objects.bulk_create(suppliers)
    ContactPerson.objects.bulk_create(suppliers_contact_person)
    StockItem.objects.bulk_create(stockitems)
    # WearStore.objects.create(id='1',name="Amar Pc",apartment='aprt',street_address='as',city='asd',state='asd',postal_code='asd',country='asd',mobile_no='asd',no_of_employees=0,area_square_ft=0)
    # SBO.objects.create(id='1',name="Amar Pc",wearhouse_id=1,apartment='aprt',street_address='as',city='asd',state='asd',postal_code='asd',country='asd',mobile_no='asd',no_of_employees=0,area_square_ft=0)
    BarcodeInfo.objects.bulk_create(bcinfo)
    BarcodeItem.objects.bulk_create(bcitem)
    OldPurchaseInfo.objects.bulk_create(oldpurchaseinfo)
    OldPurchaseDetails.objects.bulk_create(oldpurchasedetails)
    OldSalesInfo.objects.bulk_create(oldsalesinfo)
    OldSalesDetails.objects.bulk_create(oldsalesdetails)


    str = 'SELECT setval(\'asiflikk77."Barcode_barcodeitem_id_seq"\', (SELECT MAX(id) FROM asiflikk77."Barcode_barcodeitem"));'
    str = str + 'SELECT setval(\'asiflikk77."Barcode_barcodeinfo_id_seq"\', (SELECT MAX(id) FROM asiflikk77."Barcode_barcodeinfo"));'
    str = str + 'SELECT setval(\'asiflikk77."Customer_customer_id_seq"\', (SELECT MAX(id) FROM asiflikk77."Customer_customer"));'
    str = str + 'select setval(\'asiflikk77."ItemManagement_itemcategory_id_seq"\', (SELECT MAX(id) FROM asiflikk77."ItemManagement_itemcategory"));'
    str = str + 'SELECT setval(\'asiflikk77."ItemManagement_item_id_seq"\', (SELECT MAX(id) FROM asiflikk77."ItemManagement_item"));'
    str = str + 'SELECT setval(\'asiflikk77."Material_stockitem_id_seq"\', (SELECT MAX(id) FROM asiflikk77."Material_stockitem"));'
    str = str + 'SELECT setval(\'asiflikk77."Supplier_supplier_id_seq"\', (SELECT MAX(id) FROM asiflikk77."Supplier_supplier"));'
    str = str + 'SELECT setval(\'asiflikk77."Supplier_contactperson_id_seq"\', (SELECT MAX(id) FROM asiflikk77."Supplier_contactperson"));'
    str = str + 'SELECT setval(\'asiflikk77."ItemManagement_productmeta_id_seq"\', (SELECT MAX(id) FROM asiflikk77."ItemManagement_productmeta"));'
    cursor.execute(str)

#pip install django-extensions 
#python manage.py runscript migrate_tenant_data
