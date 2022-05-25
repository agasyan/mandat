-- psql -U mandat -h localhost -p 5432
DROP TABLE IF EXISTS invoice_status;
CREATE TABLE invoice_status(
   id_invoice_status INT PRIMARY KEY,
   invoice_status_name VARCHAR(255) UNIQUE NOT NULL
);

DROP TABLE IF EXISTS tipe_pengeluaran;
CREATE TABLE tipe_pengeluaran(
   id_tipe_pengeluaran INT PRIMARY KEY,
   tipe_pengeluaran_name VARCHAR(255) UNIQUE NOT NULL
);

DROP TABLE IF EXISTS project_status;
CREATE TABLE project_status(
   id_project_status INT PRIMARY KEY,
   project_status_name VARCHAR(255) UNIQUE NOT NULL
);

DROP TABLE IF EXISTS karyawan;
CREATE TABLE karyawan(
   id_karyawan INT PRIMARY KEY,
   nama VARCHAR(255) UNIQUE NOT NULL
   email VARCHAR(255) UNIQUE NOT NULL
);

DROP TABLE IF EXISTS client;
CREATE TABLE client(
   id_client INT PRIMARY KEY,
   nama VARCHAR(255) UNIQUE NOT NULL
   email VARCHAR(255) UNIQUE NOT NULL
);

DROP TABLE IF EXISTS project;
CREATE TABLE project(
   id_project INT PRIMARY KEY,
   id_client INT NOT NULL,
   id_project_manager INT NOT NULL,
   project_name VARCHAR(255) NOT NULL,
   project_value real NOT NULL,
   project_description text not null,
   start_date DATE not null,
   end_date DATE not null,
   id_project_status INT NOT NULL,
   FOREIGN KEY (id_project_status) REFERENCES project_status (id_project_status),
   FOREIGN KEY (id_project_manager) REFERENCES karyawan (id_karyawan),
   FOREIGN KEY (id_client) REFERENCES client (id_client),
);

DROP TABLE IF EXISTS invoice;
CREATE TABLE invoice(
   id_invoice INT PRIMARY KEY,
   id_project INT NOT NULL,
   invoice_desc TEXT NOT NULL,
   payment_value real NOT NULL,
   id_invoice_status INT NOT NULL,
   FOREIGN KEY (id_invoice_status) REFERENCES invoice_status (id_invoice_status),
   FOREIGN KEY (id_project) REFERENCES project_id (id_project),
);

DROP TABLE IF EXISTS pengeluaran;
CREATE TABLE pengeluaran(
   id_pengeluaran INT PRIMARY KEY,
   id_project INT NOT NULL,
   pengeluaran_name VARCHAR(255) NOT NULL,
   pengeluaran_desc TEXT NOT NULL,
   pengeluaran_value real NOT NULL,
   id_pengeluaran_status INT NOT NULL,
   FOREIGN KEY (id_pengeluaran_status) REFERENCES pengeluaran_status (id_pengeluaran_status),
   FOREIGN KEY (id_project) REFERENCES project_id (id_project),
);