import time

class TrafficLigth:

    def __init__(self):
        self.__color = color = ('RED', "YELLOW", "GREEN")

    def running(self):
        print('ВКЛ')
        while True:
            print(self.__color[0])
            time.sleep(7)
            print(self.__color[1])
            time.sleep(2)
            print(self.__color[2])
            time.sleep(5)
            print(self.__color[1])
            time.sleep(2)


traf = TrafficLigth()
traf.running()

