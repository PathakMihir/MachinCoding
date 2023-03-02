from ParkingLot.Strategy.strategy import Strategy
from slotState import States


class NearestSlotFirst(Strategy):

    def getAvailableSpot(self,floors,vehicle):

        for floor in floors:
            if floor.emptySlots[vehicle.type] > 0:
                for slot in floor.slots:
                    if slot.type == vehicle.type and slot.status == States.EMPTY:
                        return floor.id,slot.id

        return -1,-1