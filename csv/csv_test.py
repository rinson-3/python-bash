import csv

f=open("csv_file.txt")
csv_f=csv.reader(f)

for row in csv_f:
    name, phone, role =row
    print(f"Name:{name}, Phone:{phone}, Role:{role}")

f.close()


hosts=[["workstatio.local", "192.168.25.46"],["webserver.cloud", "10.2.5.6"]]
with open("host.csv", "w") as hosts_csv:
    writer=csv.writer(hosts_csv)
    writer.writerows(hosts)

# reading/writing csv using dictionaries

with open("software.csv") as software:
    reader=csv.DictReader(software)
    for row in reader:
        print(f"{row['name']} has {row['users']} users")



users=[{"name":"Sol Mansi", "username": "solm", "department":"IT infra"}, {"name": "Lio Neson", "username": "lion", "department":"USx"},{"name": "Rinson Ne", "username": "lionking", "department":"deveopmet"}]

keys=["name", "username", "department"]
with open("departments.csv", "w") as by_department:
    writer=csv.DictWriter(by_department, fieldnames=keys)
    writer.writeheader()
    writer.writerows(users)

