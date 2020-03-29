
def insertPassenger(dictionary, key, value):
    dictionary[key] = value

def searchSeat(dictionary, name):
    if dictionary[name] == None:
        return "There is no passenger with that name"
    else:
        return dictionary[name]

def removePassenger(dictionary, name):
    if dictionary[name] != None:
        del dictionary[name]
        return name + "is removed"
    else: 
        return "There is no passenger with that name"


if __name__ == "__main__":
    passenger_seat = dict()
    in_session = True
    while(in_session):
        action = input("Please enter: 1 for Insert, 2 for Search , 3 for Delete, 0 for End: ")
        action = int(action)
        if action == 1:
            name = input("Please insert name: ")
            seat = input("Please insert seat: ")
            insertPassenger(passenger_seat,name, seat)
        elif action == 2:
            name = input("Please insert name: ")
            print(searchSeat(passenger_seat, name))
        elif action == 3:
            name = input("Please insert name: ")
            print(removePassenger(passenger_seat, name))
        elif action == 0:
            in_session = False
        else:
            print("Wrong input")

        
