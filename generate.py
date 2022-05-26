from random import random
from faker import Faker
import numpy as np

def main():
    fake = Faker()
    n = 500

    # table_name karyawan
    id_k = 1
    karyawan_arr = []
    for _ in range(n):
        dct = {}
        dct["id_karyawan"] = id_k
        gender = np.random.choice(["M", "F"], p=[0.5, 0.5])
        first_name = fake.first_name_male() if gender =="M" else fake.first_name_female()
        last_name = fake.last_name()
        dct["karyawan_nama"] = f"{first_name} {last_name}"
        dct["karyawan_email"] = f"{(first_name).lower()}.{(last_name).lower()}@{fake.domain_name()}"
        karyawan_arr.append(dct)
        id_k += 1

    f = open("out.sql", "w")
    for i in karyawan_arr:
        k = ",".join(list(i.keys()))
        v = ",".join(getValues(i))
        f.write(f"INSERT INTO KARYAWAN({k}) VALUES({v});\n")
    f.close()

    #open and read the file after the appending:
    f = open("out.sql", "r")
    print(f.read())

def getValues(dict):
    list = []
    for val in dict.values():
        if isinstance(val, int):
            val = str(val)
            list.append(val)
        elif isinstance(val, str):
            list.append(f"'{val}'")
    return list

if __name__ == "__main__":
    main()