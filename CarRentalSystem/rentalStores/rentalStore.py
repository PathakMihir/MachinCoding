from .inventoryManager import InventoryManager


class RentalStores():
    __id = 1

    def __init__(self, name, location):
        self.id = RentalStores.__id
        self.name = name
        self.location = location
        self.inventoryManager = InventoryManager()
        self.reservationList=[]

    def getVehicles(self):
        return self.inventoryManager.vehicles


