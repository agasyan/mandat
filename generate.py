import random
import numpy as np


from faker import Faker
from datetime import date, datetime, timedelta


def main():
    fake = Faker()
    # project num
    n = 500

    # table_name karyawan
    id_k = 1
    karyawan_arr = []
    for _ in range(n//5):
        dct = {}
        dct["id_karyawan"] = id_k
        gender = np.random.choice(["M", "F"], p=[0.5, 0.5])
        first_name = fake.first_name_male() if gender =="M" else fake.first_name_female()
        last_name = fake.last_name()
        dct["karyawan_nama"] = f"{first_name} {last_name}"
        dct["karyawan_email"] = f"{(first_name).lower()}.{(last_name).lower()}@{fake.domain_name()}"
        karyawan_arr.append(dct)
        id_k += 1
    
    # table_name client
    id_c = 1
    client_arr = []
    for _ in range(n//5):
        dct = {}
        dct["id_client"] = id_c
        gender = np.random.choice(["M", "F"], p=[0.5, 0.5])
        first_name = fake.first_name_male() if gender =="M" else fake.first_name_female()
        last_name = fake.last_name()
        dct["client_nama"] = f"{first_name} {last_name}"
        dct["client_email"] = f"{(first_name).lower()}.{(last_name).lower()}@{fake.domain_name()}"
        dct["client_company"] = fake.company()
        client_arr.append(dct)
        id_c += 1

    ivs_arr = [{'id_invoice_status':1,'invoice_status_name':'PAID'}, {'id_invoice_status':2,'invoice_status_name':'UNPAID'}, {'id_invoice_status':3,'invoice_status_name':'DRAFT'}]
    tp_arr = [{'id_tipe_pengeluaran':1,'tipe_pengeluaran_name':'VENDOR'},{'id_tipe_pengeluaran':2,'tipe_pengeluaran_name':'OPERATION'}, {'id_tipe_pengeluaran':3,'tipe_pengeluaran_name':'TAX'}]
    ps_arr = [{'id_project_status':1,'project_status_name':'DONE'},{'id_project_status':2,'project_status_name':'REJECTED'}, {'id_project_status':3,'project_status_name':'IN PROGRESS'}]


    id_inv = 0
    id_pengeluaran = 0

    f = open("out.sql", "w")
    for i in ivs_arr:
        k = ",".join(list(i.keys()))
        v = ",".join(getValues(i))
        f.write(f"INSERT INTO invoice_status({k}) VALUES({v});\n")
    for i in tp_arr:
        k = ",".join(list(i.keys()))
        v = ",".join(getValues(i))
        f.write(f"INSERT INTO tipe_pengeluaran({k}) VALUES({v});\n")
    for i in ps_arr:
        k = ",".join(list(i.keys()))
        v = ",".join(getValues(i))
        f.write(f"INSERT INTO project_status({k}) VALUES({v});\n")
    for i in karyawan_arr:
        k = ",".join(list(i.keys()))
        v = ",".join(getValues(i))
        f.write(f"INSERT INTO karyawan({k}) VALUES({v});\n")
    for i in client_arr:
        k = ",".join(list(i.keys()))
        v = ",".join(getValues(i))
        f.write(f"INSERT INTO client({k}) VALUES({v});\n")
    f.close()

    for _ in range(100):
        print(random.randrange(30, 360, 30))
    random_date_time_list_sorted(10)
    
def getValues(dict):
    list = []
    for val in dict.values():
        if isinstance(val, int):
            val = str(val)
            list.append(val)
        elif isinstance(val, str):
            list.append(f"'{val}'")
    return list

def random_date_time_list_sorted(n):
    min_year=2016
    max_year=2021
    start_date = datetime(min_year, 1, 1)
    end_date = datetime(max_year, 12, 31)
    time_between_dates = end_date - start_date
    days_between_dates = time_between_dates.days
    date_arr = []
    for _ in range(n):
        random_number_of_days = random.randrange(days_between_dates)
        random_date = start_date + timedelta(days=random_number_of_days)
        date_arr.append(random_date)
    date_arr.sort()
    print(date_arr)
    return date_arr

if __name__ == "__main__":
    main()