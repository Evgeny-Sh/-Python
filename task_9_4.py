class Car:
    def __init__(self, name, color, speed, is_police):
        self.name = name
        self.color = color
        self.speed = speed
        self.is_police = is_police

    def go(self):
        print('GO')

    def stop(self):
        print('STOP')

    def turn(self, direction):
        print(f'Turn {direction}')

    def show_speed(self):
        print(f'Current speed: {self.speed} km/h')


class TownCar(Car):
    def __init__(self, name, color, speed):
        super().__init__(name, color, speed, False)

    def show_speed(self):
        if self.speed > 60:
            print(f'WARNING: speed limit 60 km/h.\nCurrent speed {self.speed} km/h')
        else:
            print(f'Current speed: {self.speed} km/h')


class SportCar(Car):
    def __init__(self, name, color, speed):
        super().__init__(name, color, speed, False)


class WorkCar(Car):
    def __init__(self, name, color, speed):
        super().__init__(name, color, speed, False)

    def show_speed(self):
        if self.speed > 40:
            print(f'Current speed {self.speed} km/h\nWARNING: speed limit 40 km/h.')
        else:
            print(f'Current speed: {self.speed} km/h')


class PoliceCar(Car):
    def __init__(self, name, color, speed):
        super().__init__(name, color, speed, True)


if __name__ == '__main__':
    car_1 = TownCar('Toyota', 'red', 100)
    car_2 = SportCar('Ferrari', 'white', 200)
    car_3 = WorkCar('Kamaz', 'yellow', 50)
    car_4 = PoliceCar('Lada', 'white_blue', 45)

    for car in [car_1, car_2, car_3, car_4]:
        print(car.name)
        print(car.color)
        print(car.speed)
        print(car.is_police)
        car.go()
        car.turn('left')
        car.show_speed()
        car.stop()
        print()
