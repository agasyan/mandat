import random
import numpy as np
from faker import Faker
from datetime import  datetime, timedelta
import json
import pymongo
import urllib.parse


def main():
    fake = Faker()
    # project num
    n = 50

    start = datetime.now()

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
        dct["client_nama"] = cleanStr(f"{first_name} {last_name}")
        dct["client_email"] = f"{(first_name).lower()}.{(last_name).lower()}@{fake.domain_name()}"
        dct["client_company"] = f"{fake.safe_color_name()} {fake.company()} {cleanStr(fake.country())}"
        client_arr.append(dct)
        id_c += 1

    ivs_arr = [{'id_invoice_status':1,'invoice_status_name':'PAID'}, {'id_invoice_status':2,'invoice_status_name':'UNPAID'}]
    tp_arr = [{'id_tipe_pengeluaran':1,'tipe_pengeluaran_name':'VENDOR'},{'id_tipe_pengeluaran':2,'tipe_pengeluaran_name':'OPERATION'}, {'id_tipe_pengeluaran':3,'tipe_pengeluaran_name':'TAX'}]
    ps_arr = [{'id_project_status':1,'project_status_name':'DONE'},{'id_project_status':2,'project_status_name':'REJECTED'}, {'id_project_status':3,'project_status_name':'IN PROGRESS'}]


    id_pro = 1
    id_inv = 1
    id_pengeluaran = 1

    date_arr = random_date_time_list_sorted(n)
    proj_arr = []
    inv_arr = []
    pengeluaran_arr = []
    goods = ["food", "clothes", "car", "motorcycle"]

    proj_new_dct_arr = []
    for _ in range(n):
        dct = {}
        sdate = date_arr.pop(0)
        end_date = sdate + timedelta(days=random.randrange(30, 360, 30))
        dct["project_name"] = f"{fake.safe_color_name()} {random.choice(goods)} from {cleanStr(fake.country())} to {cleanStr(fake.country())}"
        dct["project_value"] = random.randrange(10000000, 1000000000, 1000000)
        dct["project_description"] = fake.paragraph(nb_sentences=2)
        dct["start_date"] = sdate
        dct["end_date"] = end_date
        dct["id_project"] = id_pro

        # get 
        ps =  np.random.choice(ps_arr, p=[0.6, 0.2, 0.2])
        client = random.choice(client_arr)
        pm = random.choice(karyawan_arr)

        # new_dct for json obj
        new_dct = dct.copy()
        new_dct["_id"] = id_pro
        new_dct["project_status"] = ps
        new_dct["client"] = client
        new_dct["project_manager"] = pm
        
        
        dct["id_client"] = client["id_client"]
        dct["id_project_manager"] = pm["id_karyawan"]
        dct["id_project_status"] = ps["id_project_status"]
        proj_arr.append(dct)
        # Done
        proj_inv_arr = [] 
        proj_klr_arr = []
        if ps["id_project_status"] != 2:
            # Generate Invoice
            inv_count = random.randrange(1, 4)
            split_inv = randomList(inv_count, 100)
            for i in range(inv_count):
                inv = {}
                inv["id_invoice"] = id_inv
                inv["id_project"] = id_pro
                inv["invoice_desc"] = fake.paragraph(nb_sentences=2)
                inv["payment_value"] = (dct["project_value"] * split_inv[i]) // 100
                inv["id_invoice_status"] = random.choice(ivs_arr)["id_invoice_status"]
                if ps["id_project_status"] == 1 :
                    inv["id_invoice_status"] = ivs_arr[0]["id_invoice_status"]
                inv_arr.append(inv)
                proj_inv_arr.append(inv)
                id_inv += 1
    
            # Generate Pengeluaran
            pengeluaran_count = random.randrange(1, 6)
            split_pglrn = randomList(pengeluaran_count, random.randrange(60, 120))
            for i in range(pengeluaran_count):
                pengeluaran = {}
                pengeluaran["id_pengeluaran"] = id_pengeluaran
                pengeluaran["id_project"] = id_pro
                tpeng = random.choice(tp_arr)
                tp_name =tpeng["tipe_pengeluaran_name"]
                pengeluaran["pengeluaran_name"] = f"Pengeluaran untuk {tp_name} Project ID: {id_pro}"
                pengeluaran["pengeluaran_desc"] = fake.paragraph(nb_sentences=2)
                pengeluaran["pengeluaran_value"] = (dct["project_value"] * split_pglrn[i]) // 100
                pengeluaran["id_tipe_pengeluaran"] = tpeng["id_tipe_pengeluaran"]
                pengeluaran_arr.append(pengeluaran)
                proj_klr_arr.append(pengeluaran)
                id_pengeluaran += 1
            new_dct["invoice"] = proj_inv_arr
            new_dct["pengeluaran"] = proj_klr_arr
        proj_new_dct_arr.append(new_dct)
        id_pro += 1

    # convert into json
    # file name is mydata
    with open("out.json", "w") as final:
        json.dump(proj_new_dct_arr, final, default=json_serial)
    f = open("out.sql", "w")
    for chnk in chunks(ivs_arr, 100):
        k = ""
        v_arr = []
        for item in chnk: 
            k = ",".join(list(item.keys()))
            v = ",".join(getValues(item))
            v = f"({v})"
            v_arr.append(v)
        vals = ",".join(v_arr)
        f.write(f"INSERT INTO invoice_status({k}) VALUES {vals};\n")
    for chnk in chunks(tp_arr, 100):
        k = ""
        v_arr = []
        for item in chnk: 
            k = ",".join(list(item.keys()))
            v = ",".join(getValues(item))
            v = f"({v})"
            v_arr.append(v)
        vals = ",".join(v_arr)
        f.write(f"INSERT INTO tipe_pengeluaran({k}) VALUES {vals};\n")
    for chnk in chunks(ps_arr, 100):
        k = ""
        v_arr = []
        for item in chnk: 
            k = ",".join(list(item.keys()))
            v = ",".join(getValues(item))
            v = f"({v})"
            v_arr.append(v)
        vals = ",".join(v_arr)
        f.write(f"INSERT INTO project_status({k}) VALUES {vals};\n")
    for chnk in chunks(karyawan_arr, 100):
        k = ""
        v_arr = []
        for item in chnk: 
            k = ",".join(list(item.keys()))
            v = ",".join(getValues(item))
            v = f"({v})"
            v_arr.append(v)
        vals = ",".join(v_arr)
        f.write(f"INSERT INTO karyawan({k}) VALUES {vals};\n")
    for chnk in chunks(client_arr, 100):
        k = ""
        v_arr = []
        for item in chnk: 
            k = ",".join(list(item.keys()))
            v = ",".join(getValues(item))
            v = f"({v})"
            v_arr.append(v)
        vals = ",".join(v_arr)
        f.write(f"INSERT INTO client({k}) VALUES {vals};\n")
    for chnk in chunks(proj_arr, 100):
        k = ""
        v_arr = []
        for item in chnk: 
            k = ",".join(list(item.keys()))
            v = ",".join(getValues(item))
            v = f"({v})"
            v_arr.append(v)
        vals = ",".join(v_arr)
        f.write(f"INSERT INTO project({k}) VALUES {vals};\n")
    for chnk in chunks(inv_arr, 100):
        k = ""
        v_arr = []
        for item in chnk: 
            k = ",".join(list(item.keys()))
            v = ",".join(getValues(item))
            v = f"({v})"
            v_arr.append(v)
        vals = ",".join(v_arr)
        f.write(f"INSERT INTO invoice({k}) VALUES {vals};\n")
    for chnk in chunks(pengeluaran_arr, 100):
        k = ""
        v_arr = []
        for item in chnk: 
            k = ",".join(list(item.keys()))
            v = ",".join(getValues(item))
            v = f"({v})"
            v_arr.append(v)
        vals = ",".join(v_arr)
        f.write(f"INSERT INTO pengeluaran({k}) VALUES {vals};\n")
    f.close()

    end = datetime.now()
    res = end - start
    print(res)
    res_ms = int(res.total_seconds() * 1000) # milliseconds
    print(res_ms)

    import_mongo = False
    smdb = datetime.now()
    if import_mongo:
        username = urllib.parse.quote_plus('mandat')
        password = urllib.parse.quote_plus('mandat')
        myclient = pymongo.MongoClient('mongodb://%s:%s@localhost:27017/mandat-db' % (username, password))
        mydb = myclient["mandat-db"]
        mycol = mydb["projects"]
        x = mycol.insert_many(proj_new_dct_arr)
        #print list of the _id values of the inserted documents:
        print(x.inserted_ids)
    emdb = datetime.now()
    res = emdb - smdb
    res_ms = int(res.total_seconds() * 1000) # milliseconds
    print(res_ms)

def randomList(length, sum):
    arr = [0] * length
    for _ in range(sum) :
        arr[random.randint(0, sum) % length] += 1
    return arr
    
def getValues(dict):
    list = []
    for val in dict.values():
        if isinstance(val, int):
            val = str(val)
            list.append(val)
        elif isinstance(val, str):
            list.append(f"'{val}'")
        elif isinstance(val, datetime):
            date_time = val.strftime("%Y-%m-%d %H:%M:%S")
            list.append(f"'{date_time}'")
    return list

def cleanStr(input):
    s = ''.join(ch for ch in input if ch.isalnum() or ch == ' ')
    return s

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
    return date_arr

def chunks(l, n):
    n = max(1, n)
    return (l[i:i+n] for i in range(0, len(l), n))

def json_serial(obj):
    """JSON serializer for objects not serializable by default json code"""

    if isinstance(obj, (datetime)):
        return obj.isoformat()
    raise TypeError ("Type %s not serializable" % type(obj))

if __name__ == "__main__":
    main()