from abc import ABC, abstractmethod


class vehicle(ABC):

    @abstractmethod
    def start(self):
        pass



class car(vehicle):
    def start(self):
        print("car is starting")


class bike(vehicle):
    def start(self):
        print("bike startts with key")

c1 = car()
b1 = bike()


c1.start()
b1.start()





