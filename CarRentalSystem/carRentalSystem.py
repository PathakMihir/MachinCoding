import datetime

from CarRentalSystem.users.user import User
from CarRentalSystem.users.userController import UserController
from CarRentalSystem.vehicles.suv import SUV
from CarRentalSystem.location import Location
from CarRentalSystem.rentalStores.rentalStore import RentalStores
from CarRentalSystem.reservation import Reservation
from CarRentalSystem.billing import Billing
from CarRentalSystem.payment import Payment

class CarRentalSystem():

    def __init__(self):
        self.userController = UserController()
        self.rentalStores = []
        self.billing = Billing()

    def getStoresByLocation(self, city, state, pincode):
        sol = []
        for stores in self.rentalStores:
            print(stores)
            if stores.location.city == city and stores.location.state == state and stores.location.pincode == pincode:
                sol.append(stores)
        return sol

    def vehicleListForStore(self, store):
        return store.inventoryManagement.getVehicles()

    def createReservation(self, store, user, vehicle, date, startTime, endTime, duration):
        # check vehicle if time slot is availableand then reserve
        reservation=Reservation(user, vehicle, date, startTime, endTime, duration)
        store.reservationList.append(reservation)
        # and update everywhere about the time slot
        vehicle.UpdateSlot(date, startTime, endTime)
        user.reservations.append(reservation)

    def addUser(self, user):
        self.userController.addUser(user)

    def getUser(self, name):
        return self.userController.getUser(name)

    def addStores(self, store):
        self.rentalStores.append(store)

    def dropOFF(self):
        pass

    def calulcateBill(self, reservation):
        return self.billing.calculateBill(reservation)


if __name__ == "__main__":
    rentalSystem = CarRentalSystem()
    location = Location("BANGALORE", "KARNATAKA", "444602")

    # Add User
    rentalSystem.addUser(User("U1", "2312312312"))
    u1 = rentalSystem.getUser("U1")
    rentalSystem.addUser(User("U2", "2312312312"))

    # addVehicles
    v1 = SUV(name="FORTUNER", location=location, price=1000)
    v2 = SUV(name="DUSTER", location=location, price=1000)

    # addStores
    store1 = RentalStores("BANGLORE1", location)
    store2 = RentalStores("BANGLORE2", location)

    store1.inventoryManager.addVehicles(v1)
    store2.inventoryManager.addVehicles(v2)

    rentalSystem.addStores(store1)
    rentalSystem.addStores(store2)

    # Find vehicle from a store in a particular location
    stores = rentalSystem.getStoresByLocation("BANGALORE", "KARNATAKA", "444602")
    bookingVehicle = stores[0].getVehicles()[0]
    print(bookingVehicle)
    # Find vehicles in particular stores with timings
    print(bookingVehicle.dateTimeSlots)

    date = datetime.date.today()
    startTime = datetime.datetime.now()
    endTime = datetime.datetime.now()
    # endTime=startTime+datetime.time.hour
    print(date, startTime)
    # Create reservation
    rentalSystem.createReservation(stores[0], u1, bookingVehicle,date, startTime, endTime, 3)
    print(u1.reservations[0].vehicle)
    amount=rentalSystem.calulcateBill(u1.reservations[0])
    print(amount)
    u1.addPayment(Payment("234234234"))
    print(u1.payment.doPayment(amount,"213123"))