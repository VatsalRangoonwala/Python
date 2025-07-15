# Write a Class ‘Train’ which has methods to book a ticket, get status (no of seats) 
# and get fare information of train running under Indian Railways.
import random

class Train:
    # def __init__(self, n, frm, to):
    #     self.n = n
    #     self.frm = frm
    #     self.to = to
    frm = input("From: ")
    to = input("To: ")
    n = random.randint(99999, 1000000)
    seats = random.randint(90, 700)

    def getFare(self):
        print("\n\tTicket is booked")
        print(f"Train no: {self.n}")
        print(f"From '{self.frm}' To '{self.to}'")

    def getStatus(self):
        print(f"Total Available seats: {self.seats}")
        print("Your train is running on time")

a = Train()
a.getFare()
a.getStatus()