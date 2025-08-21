import csv
import uuid
CSV_FILE = "python-csv-practice/data.csv" # CSV File Path

rows = [
    ["Name", "Age", "City"],
    ["Rafi", 20, "Chittagong"],
    ["Mamun", 21, "Dhaka"],
]                                               # output ------->
with open(CSV_FILE, "w", newline="") as file:   # Name,Age,City
    writer = csv.writer(file)                   # Rafi,20,Chittagong
    writer.writerows(rows)                      # Mamun,21,Dhaka
#-------------------------------------------------------------------------
ID = uuid.uuid4()                                   
with open(CSV_FILE, "w", newline="") as file:       
    writer = csv.writer(file)                       # output ---->
    writer.writerows([["Name", "Age", "City"]])     # Name,Age,City
    writer.writerow(["Rafi", 30, "dhaka"])          # Rafi,30,dhaka
    writer.writerow([ID])                           # aadc28d9-ab53-4bf1-b13b-cd2c43911251
#-------------------------------------------------------------------------
rows = [
    {"Name":"Rafi", "Age":20, "City":"Chittagong"},
    {"Name":"Mamun", "Age":23, "City":"Dhaka"},
]
with open(CSV_FILE, "w", newline="") as file:
    fieldname = ["Name", "Age", "City"]                             # Output---->
    writer = csv.DictWriter(file, fieldnames=fieldname)             # RName,Age,City
    writer.writeheader()# Write header column name                  # Rafi,20,Chittagong
    writer.writerows(rows)# write the data in 'rows' <-variable     # Mamun,23,Dhaka
#-----------
## Appending New Rows --->                          # Output ---->
new_rows = ['Hasan', 50, 'Khulna']                  # Name,Age,City
with open(CSV_FILE, 'a', newline="") as file:       # Rafi,20,Chittagong
    writer = csv.writer(file)                       # Mamun,23,Dhaka
    writer.writerow(new_rows)                       # Hasan,50,Khulna <-- New added
#-------------------------------------------------------------------------




