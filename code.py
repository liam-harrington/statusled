from time import sleep
from lib import RGBLED, Status, StatusLED

rgbled = RGBLED('D1', 'D2', 'D3')

statusled = StatusLED(led=rgbled)

statusled.set(Status.INFO)
#statusled.set(Status.WARN)
#statusled.set(Status.DANG)
#statusled.set(Status.EMER)
#statusled.set(Status.SUCC)

sleep(1.0)

while True:
    statusled.expose()

