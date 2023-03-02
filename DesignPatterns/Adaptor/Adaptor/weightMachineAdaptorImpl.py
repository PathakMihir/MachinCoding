from DesignPatterns.Adaptor.Adaptor.weightMachineAdaptor import WeightMachineAdaptor
from DesignPatterns.Adaptor.Adaptee.weightMachineForBabies import WeightMachineForBabies

class WeightMachineAdaptorImpl(WeightMachineAdaptor):

    def __init__(self, weightMachine):
        self.weightMachine = weightMachine

    def getWeightInKg(self):
        return self.weightMachine.getWeightInPound() * 1.5



if __name__=="__main__":
    adaptee=WeightMachineForBabies()
    adaptor=WeightMachineAdaptorImpl(adaptee)
    print(adaptor.getWeightInKg())