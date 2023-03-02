from collections import defaultdict


class User:

    def __init__(self, name, license_number):
        self.name = name
        self.license_number = license_number
        self.reservations=[]

    def addPayment(self,payment):
        self.payment=payment
