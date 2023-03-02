from ParkingLot.slotState import States
from ParkingLot.ticket import Ticket
from Strategy.nearestSlotFirst import NearestSlotFirst


class ParkingLot:
    _id = 1
    def __init__(self):
        self.id = ParkingLot._id
        ParkingLot._id += 1
        self.floors = []
        self.tickets = []
        self.strategy = NearestSlotFirst()

    def parkVehicle(self, vehicle):

        floor, slot = self.strategy.getAvailableSpot(self.floors, vehicle)
        if floor != -1 and slot != -1:
            slot.status = States.RESERVED
            generatedTicket = Ticket(self.id, floor.id, slot.id, vehicle)
            self.tickets.append(generatedTicket)
            floor.emptySlots[slot.type] -= 1
            return "SUCCESS"
        return "FAILED"

    def unParkVehicle(self, ticket):
        parking_lot = ticket.parkingLot
        floor = ticket.floor
        slot = ticket.slot
        self.floors[floor - 1].slots[slot - 1].status = States.EMPTY
        self.floors[floor - 1].emptySlots[slot] += 1

    def checkForSpace(self, vehicle):

        for floor in self.floors:
            if floor.emptySlots[vehicle.type] > 0:
                return True

        return False

    def addFloor(self, floor):
        self.floors.append(floor)

    def getSpaceForSpecifcType(self):
        pass

if __name__=="__main__":

