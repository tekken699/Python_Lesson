class Car:
    def __init__(self, name, color,speed, ispolice=None):
        self.name = name
        self.color = color
        self.speed = speed
        self.isPolice = ispolice

    def show_speed(self):
        return f'{self.name} is moving at a speed {self.speed}km/h'

    def go(self):
        print(f'{self.name} GO-GO !')

    def stop(self,):
        print(f'{self.name} stop !')

    def turn(self, direction):
        print(f'{self.name} turned {direction} !')


class TownCar(Car):
    def show_speed(self):
        print(f'{self.speed} OVER SPEED!' if self.speed > 60 else super().show_speed())

class SportCar(Car):
    pass

class WorkCar(Car):
    def show_speed(self):
        print(f'{self.speed} OVER SPEED!' if self.speed > 40 else super().show_speed())


class PoliceCar(Car):
    pass

bus = TownCar('Bus', 'Blue', 80)
bus.go()
bus.show_speed()
bus.turn('Left')
bus.stop()
print('**********************************')
sport = WorkCar('Mazda', 'Red', 40)
sport.go()
sport.show_speed()
sport.turn('Left')
sport.stop()

