from time import sleep


class TrafficLight:
    __color = 'red'

    def running(self):
        for c, t in (('red', 7), ('yellow', 2), ('green', 5)):
            __color = c
            for i in range(t, 0, -1):
                print(f'Traffic light: {__color} {i}', end='\n')
                sleep(1)


if __name__ == '__main__':
    tl = TrafficLight()
    tl.running()
