-- invoice_status
INSERT INTO invoice_status(id_invoice_status, invoice_status_name) VALUES(1,'PAID');
INSERT INTO invoice_status(id_invoice_status, invoice_status_name) VALUES(2,'UNPAID');
INSERT INTO invoice_status(id_invoice_status, invoice_status_name) VALUES(3,'DRAFT');

-- tipe_pengeluaran
INSERT INTO tipe_pengeluaran(id_tipe_pengeluaran, tipe_pengeluaran_name) VALUES(1,'VENDOR');
INSERT INTO tipe_pengeluaran(id_tipe_pengeluaran, tipe_pengeluaran_name) VALUES(2,'OPERATION');
INSERT INTO tipe_pengeluaran(id_tipe_pengeluaran, tipe_pengeluaran_name) VALUES(3,'TAX');

-- project_status
INSERT INTO project_status(id_project_status, project_status_name) VALUES(1,'DONE');
INSERT INTO project_status(id_project_status, project_status_name) VALUES(2,'REJECTED');
INSERT INTO project_status(id_project_status, project_status_name) VALUES(3,'IN PROGRESS');

-- karyawan
INSERT INTO KARYAWAN(id_karyawan,name,email) VALUES(1,'GeraldAnderson','gerald.anderson@young-saunders.com')
INSERT INTO KARYAWAN(id_karyawan,name,email) VALUES(2,'RavenThompson','raven.thompson@pena.biz')
INSERT INTO KARYAWAN(id_karyawan,name,email) VALUES(3,'DonnaGarza','donna.garza@mcguire-brown.org')
INSERT INTO KARYAWAN(id_karyawan,name,email) VALUES(4,'ThomasMurphy','thomas.murphy@mueller.com')
INSERT INTO KARYAWAN(id_karyawan,name,email) VALUES(5,'KyleMartin','kyle.martin@jones-wood.net')


