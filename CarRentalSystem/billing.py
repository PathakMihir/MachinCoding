class Billing():

    def calculateBill(self,reservation):

        return reservation.vehicle.hourlyPrice*reservation.duration
