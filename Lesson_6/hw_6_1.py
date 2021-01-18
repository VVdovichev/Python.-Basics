"""from time import sleep


class TrafficLight:
    __color = ['Красный', 'Желтый', 'Зеленый']
    red = 'Красный'
    yellow = 'Жёлтый'
    green = 'Зелёный'

    def running(self):
        while True:
            print(self.__color[])
            if i == 0:
                sleep(7)
            elif i == 1:
                sleep(2)
            elif i == 2:
                sleep(5)



Traffic = TrafficLight()
Traffic.running()"""


import time
import threading


class TrafficLight(threading.Thread):
    __color = 0

    def run(self):
        self.__color = 'red'
        print(f'Светофор: {self.__color}')
        time.sleep(7)

        self.__color = 'yellow'
        print(f'Светофор: {self.__color}')
        time.sleep(2)

        self.__color = 'green'
        print(f'Светофор: {self.__color}')
        time.sleep(5)

        while True:
            self.run()


traffic = TrafficLight()
traffic.start()





