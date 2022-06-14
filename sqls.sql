SELECT setval('asiflikk77."Barcode_barcodeinfo_id_seq"', (SELECT MAX(id) FROM asiflikk77."Barcode_barcodeinfo"));
SELECT setval('asiflikk77."Barcode_barcodeitem_id_seq"', (SELECT MAX(id) FROM asiflikk77."Barcode_barcodeitem"));
SELECT setval('asiflikk77."Customer_customer_id_seq"', (SELECT MAX(id) FROM asiflikk77."Customer_customer"));
SELECT setval('asiflikk77."Customer_creditlimit_id_seq"', (SELECT MAX(id) FROM asiflikk77."Customer_creditlimit"));
SELECT setval('asiflikk77."ItemManagement_item_id_seq"', (SELECT MAX(id) FROM asiflikk77."ItemManagement_item"));
SELECT setval('asiflikk77."ItemManagement_itemcategory_id_seq"', (SELECT MAX(id) FROM asiflikk77."ItemManagement_itemcategory"));
SELECT setval('asiflikk77."Material_stockitem_id_seq"', (SELECT MAX(id) FROM asiflikk77."Material_stockitem"));
SELECT setval('asiflikk77."Supplier_supplier_id_seq"', (SELECT MAX(id) FROM asiflikk77."Supplier_supplier"));
SELECT setval('asiflikk77."Supplier_contactperson_id_seq"', (SELECT MAX(id) FROM asiflikk77."Supplier_contactperson"));

--psql -U esecure -d XposProdDB2 -a -f sqls.sql--
