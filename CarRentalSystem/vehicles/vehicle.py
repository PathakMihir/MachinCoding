from location import Location


class Vehicle():
    _id = 1

    def __init__(self, name: str,  location: Location) -> object:
        self.id = Vehicle._id
        Vehicle._id += 1
        self.name = name
        self.location = location
        self.dateTimeSlots={}

    def UpdateSlot(self,date,startTime,endTime):
        pass

