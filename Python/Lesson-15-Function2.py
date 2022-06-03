def create_record(name, telephone, address):
    "Create Record"
    record = {
        'name': name,
        'tel': telephone,
        'address': address
    }
    return record


user1 = create_record("Stepan", "0937447744", "Lviv")
user2 = create_record("Ira", "09311111111", "Kyiv")

print(user1)
print(user2)

def give_award(medal, *persons):
    "Give Medals to persons:"
    for persons in persons:
        print("The Man " + persons + medal)

give_award("Za Lviv", "Stepan", "Iryna")
give_award("Za Kyiv", "Vasyl", "Valentyn")
