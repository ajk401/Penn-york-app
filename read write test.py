class File():

    def __init__(self, location, type):
        self.location = location
        self.type = type

    def open_file(self):
        people = {}
        Main_file = open(self.location)
        for line in Main_file:
            key, value = line.split()
            people[key] = value
            print(people)

Test = File("test.txt", 0)
Test.open_file()
