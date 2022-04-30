import sys

# get the amount of cases
cases = int(sys.stdin.readline().rstrip())

class Contact:
    def __init__(self, name, number, address, status=""):
        self.name = name
        self.number = number
        self.address = address
        self.status = status

    def __str__(self):
        return self.name + self.status

    def __eq__(self, obj):
        if not isinstance(obj, Contact):
            # don't attempt to compare against unrelated types
            return NotImplemented

        return self.name == obj.name

    def comp(self, obj):
        if self.number != obj.number and self.address != obj.address:
            self.status = " UPDATED BOTH"
        elif  self.number != obj.number:
            self.status = " UPDATED PHONE NUMBER"
        elif self.address != obj.address:
            self.status = " UPDATED ADDRESS"



for i in range(cases):
    a = sys.stdin.readline().rstrip()
    init = int(a.split(" ")[0])
    fin = int(a.split(" ")[1])

    init_contacts = []
    init_names = []
    fin_contacts = []
    fin_names = []

    for j in range(init):
        line = sys.stdin.readline().rstrip()
        spl = line.split(",")
        init_contacts.append(Contact(spl[0], spl[1], spl[2]))
        init_names.append(spl[0])
    
    for j in range(fin):
        line = sys.stdin.readline().rstrip()
        spl = line.split(",")
        fin_contacts.append(Contact(spl[0], spl[1], spl[2]))
        fin_names.append(spl[0])

    contacts = []

    for contact in fin_contacts:
        if contact not in init_contacts:
            contact.status = " CREATED"
            contacts.append(contact)

    while len(init_contacts) != 0:
        if init_contacts[0] not in fin_contacts:
            init_contacts[0].status = " DELETED"
            contacts.append(init_contacts.pop(0))
            
        else:
            for contact in fin_contacts:
                if init_contacts[0].name == contact.name:
                    init_contacts[0].comp(contact)


            if init_contacts[0].status != "":
                contacts.append(init_contacts.pop(0))
            else:
                init_contacts.pop(0)

    contacts = sorted([str(contact) for contact in contacts])

    for contact in contacts:
        print(contact)
    