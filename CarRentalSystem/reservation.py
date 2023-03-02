class Reservation():
    __id = 1

    def __init__(self, user, vehicle, date, startTime, endTime, duration):
        self.id = Reservation.__id
        Reservation.__id += 1
        self.user = user
        self.vehicle = vehicle
        self.date = date
        self.startTime = startTime
        self.endTime = endTime
        self.duration = duration
