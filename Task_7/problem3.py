
class passenger:
    pass

a = passenger()
b = passenger()
c = passenger()


class Flight:
    def __init__(self):
        self.passengers = []
    def add_passenger(self, obj_passenger):
        self.passengers.append(obj_passenger)
        print(len(self.passengers))              #for checking


total = Flight()
total.add_passenger(a)
total.add_passenger(b)
total.add_passenger(c)
