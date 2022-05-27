-- psql -U mandat -h localhost -p 5432

DROP TABLE IF EXISTS pengeluaran;
DROP TABLE IF EXISTS invoice;
DROP TABLE IF EXISTS project;
DROP TABLE IF EXISTS client;
DROP TABLE IF EXISTS karyawan;
DROP TABLE IF EXISTS project_status;
DROP TABLE IF EXISTS tipe_pengeluaran;
DROP TABLE IF EXISTS invoice_status;

CREATE TABLE invoice_status(
   id_invoice_status INT PRIMARY KEY,
   invoice_status_name VARCHAR(255) UNIQUE NOT NULL
);

CREATE TABLE tipe_pengeluaran(
   id_tipe_pengeluaran INT PRIMARY KEY,
   tipe_pengeluaran_name VARCHAR(255) UNIQUE NOT NULL
);

CREATE TABLE project_status(
   id_project_status INT PRIMARY KEY,
   project_status_name VARCHAR(255) UNIQUE NOT NULL
);

CREATE TABLE karyawan(
   id_karyawan INT PRIMARY KEY,
   karyawan_nama VARCHAR(255) UNIQUE NOT NULL,
   karyawan_email VARCHAR(255) UNIQUE NOT NULL
);

CREATE TABLE client(
   id_client INT PRIMARY KEY,
   client_nama VARCHAR(255) UNIQUE NOT NULL,
   client_email VARCHAR(255) UNIQUE NOT NULL,
   client_company VARCHAR(255) UNIQUE NOT NULL
);

CREATE TABLE project(
   id_project INT PRIMARY KEY,
   id_client INT NOT NULL,
   id_project_manager INT NOT NULL,
   project_name VARCHAR(255) NOT NULL,
   project_value INT NOT NULL,
   project_description text not null,
   start_date TIMESTAMP not null,
   end_date TIMESTAMP not null,
   id_project_status INT NOT NULL,
   FOREIGN KEY (id_project_status) REFERENCES project_status (id_project_status),
   FOREIGN KEY (id_project_manager) REFERENCES karyawan (id_karyawan),
   FOREIGN KEY (id_client) REFERENCES client (id_client)
);

CREATE TABLE invoice(
   id_invoice INT PRIMARY KEY,
   id_project INT NOT NULL,
   invoice_desc TEXT NOT NULL,
   payment_value INT NOT NULL,
   id_invoice_status INT NOT NULL,
   FOREIGN KEY (id_invoice_status) REFERENCES invoice_status (id_invoice_status),
   FOREIGN KEY (id_project) REFERENCES project (id_project)
);

CREATE TABLE pengeluaran(
   id_pengeluaran INT PRIMARY KEY,
   id_project INT NOT NULL,
   pengeluaran_name VARCHAR(255) NOT NULL,
   pengeluaran_desc TEXT NOT NULL,
   pengeluaran_value INT NOT NULL,
   id_tipe_pengeluaran INT NOT NULL,
   FOREIGN KEY (id_tipe_pengeluaran) REFERENCES tipe_pengeluaran (id_tipe_pengeluaran),
   FOREIGN KEY (id_project) REFERENCES project (id_project)
);