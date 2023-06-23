class RGBColor:

    all = list()

    def __init__(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b
        RGBColor.all.append(self)

class RGBLED:

    OFF = RGBColor(False, False, False)

    RED = RGBColor(True, False, False)
    YELLOW = RGBColor(True, True, False)

    GREEN = RGBColor(False, True, False)
    CYAN = RGBColor(False, True, True)

    BLUE = RGBColor(False, False, True)
    PINK = RGBColor(True, False, True)

    WHITE = RGBColor(True, True, True)

    INIT = WHITE
    CURRENT = None

    def __init__(self, rpin=None, gpin=None, bpin=None):
        import board

        if isinstance(rpin, str):
            rpin = getattr(board, rpin)

        if isinstance(gpin, str):
            gpin = getattr(board, gpin)
        
        if isinstance(bpin, str):
            bpin = getattr(board, bpin)



        self.rpin = rpin
        if rpin:
            self.r = RGBLED.setup(rpin)
        
        self.gpin = gpin
        if gpin:
            self.g = RGBLED.setup(gpin)

        self.bpin = bpin
        if bpin:
            self.b = RGBLED.setup(bpin)       

        if RGBLED.INIT:
            self.set(RGBLED.INIT)

    def setup(pin):
        from digitalio import DigitalInOut, Direction
        try:
            led = DigitalInOut(pin)
            led.direction = Direction.OUTPUT
            return led
        except:
            raise Exception('unable to setup led pin')

    def set(self, rgbcolor):
        RGBLED.CURRENT = rgbcolor
        self.r.value = rgbcolor.r
        self.g.value = rgbcolor.g
        self.b.value = rgbcolor.b
