from ParkingLot.vehicleType import VehicleType
class Floor:
    _id = 1

    def __init__(self):
        self.id = Floor._id
        Floor._id += 1
        self.slots = []
        self.emptySlots = {VehicleType.CAR:0,VehicleType.BIKE:0,VehicleType.TRUCK:0}

    def addSlot(self, slot):
        self.slots.append(slot)
        self.emptySlots[slot.type]+1
