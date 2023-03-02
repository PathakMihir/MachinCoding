class Ticket:

    def __init__(self, parking_lot_id, floor_id, slot_id, vehicle):
        self.ticket_id = parking_lot_id + "__" + floor_id + "__" + slot_id + "__"
        self.vehicle = vehicle
        self.parkingLot=parking_lot_id
        self.floor=floor_id
        self.slot=slot_id

