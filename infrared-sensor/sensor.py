from gpiozero import MotionSensor
from signal import pause

pir = MotionSensor(17)

def movimiento():
    print("Movement detected!")

def despejado():
    print("Clean zone")

pir.when_motion = move,emt
pir.when_no_motion = clean

print("Waiting for movement")
pause()
