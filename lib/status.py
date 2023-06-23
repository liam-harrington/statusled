from .rgb import RGBLED

class State:

    spacing = 10

    def __init__(self, name, blink=0):
        self.name = name
        self.upper = name.upper()
        self.blink = blink

class Status:

    active = True

    INFO = State('information')
    WARN = State('warning')
    DANG = State('danger', blink=4)
    EMER = State('emergency', blink=10)
    SUCC = State('success')

    #states = list()
    def __init__(self):
        self.states = list()

    def set(self, state):
        self.states.append(state)

class StatusLED(Status):

    def __init__(self, led=None, duration=5.0):
        super().__init__()
        self.led = led
        self.duration = duration

    def expose(self):
        from time import sleep
        if self.active:
            for state in self.states:
                print(state.upper)
                if state == Status.INFO:
                    self.led.set(RGBLED.CYAN)
                    sleep(self.duration)
                elif state == Status.WARN:
                    self.led.set(RGBLED.RED)
                    sleep(self.duration)
                elif state == Status.DANG:
                    i = int()
                    subduration = self.duration / state.blink / 2
                    while i < state.blink:
                        self.led.set(RGBLED.RED) # makes led blink
                        sleep(subduration)
                        self.led.set(RGBLED.OFF) # makes led blink
                        sleep(subduration)
                        i += 1
                    del(i)
                    del(subduration)
                    self.led.set(RGBLED.RED) # makes led blink
                elif state == Status.EMER:
                    i = int()
                    subduration = self.duration / state.blink / 3
                    while i < state.blink:
                        self.led.set(RGBLED.RED) # makes led blink
                        sleep(subduration)
                        self.led.set(RGBLED.OFF) # makes led blink
                        sleep(subduration)
                        self.led.set(RGBLED.YELLOW) # makes led blink
                        sleep(subduration)
                        i += 1
                    del(i)
                    del(subduration)
                    self.led.set(RGBLED.RED) # makes led blink
                elif state == Status.SUCC:
                    self.led.set(RGBLED.GREEN)
                    sleep(self.duration)

        else:
            self.led.set(RGBLED.OFF)
