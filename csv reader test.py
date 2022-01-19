import csv




filename = "datasheets/test.csv"

with open(filename, "r") as file:
    csv_reader = csv.DictReader(file)
    for line in csv_reader:
        print(line)

#    with open('datasheets/newfile.csv', 'w') as newfile:
#        csv_writer = csv.writer(newfile)
#
#        for line in csv_reader:
#            csv_writer.writerow(line)

#class File(object):
#    """docstring for ."""
#
#    def __init__(self, location):
#        self.arg = arg
