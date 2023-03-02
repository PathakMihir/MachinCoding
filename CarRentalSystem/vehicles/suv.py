from .vehicle import Vehicle


class SUV(Vehicle):

    def __init__(self, name, location, price):
        super().__init__(name, location)
        self.hourlyPrice = price
        self.type = "SUV"
