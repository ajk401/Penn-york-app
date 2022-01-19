import random, csv

def generate_id():
    id = str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9))
    with open("datasheets/stafflist.csv", "r") as stafflist:
        stafflist_id = []
        stafflist_reader = csv.DictReader(stafflist)
        for line in stafflist_reader:
            stafflist_id.append(stafflist_reader['id'])
        while id in stafflist_id:
            id = str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9))
        return id
print(generate_id())
