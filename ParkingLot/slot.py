from ParkingLot.slotState import States


class Slot:
    _id = 1

    def __init__(self, type):
        self.id = Slot._id
        Slot._id += 1
        self.type = type
        self.status = States.EMPTY
