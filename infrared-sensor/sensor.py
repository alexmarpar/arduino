from gpiozero import MotionSensor
from signal import pause

pir = MotionSensor(17)

def movimiento():
    print("Movement detected!")

def despejado():
    print("Zone cleaned")

pir.when_motion = movimiento
pir.when_no_motion = despejado

print("Waiting for movement")
pause()
