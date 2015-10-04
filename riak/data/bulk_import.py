import csv
import json
import riak

client = riak.RiakClient()
bucket = client.bucket('za')

f = open("ZA10k.csv", "r")
for row in csv.DictReader(f):
    key = row['social']
    sex = row['sex']
    blood = row['blood']
    weight = row['weight']
    state = row['state']
    item = bucket.new(key, data=row)
    if sex == "male":
        item.add_index('sex_bin', sex)
    else:
        item.add_index('sex_bin', sex)
    if blood == "A+":
        item.add_index('blood_bin', blood)
    elif blood == "A-":
        item.add_index('blood_bin', blood)
    elif blood == "B+":
        item.add_index('blood_bin', blood)
    elif blood == "B-":
        item.add_index('blood_bin', blood)
    elif blood == "O+":
        item.add_index('blood_bin', blood)
    elif blood == "O-":
        item.add_index('blood_bin', blood)
    elif blood == "AB+":
        item.add_index('blood_bin', blood)
    elif blood == "AB-":
        item.add_index('blood_bin', blood)
    item.add_index('weight_bin', weight)
    item.add_index('state_bin', state)
    item.store()
f.close()
