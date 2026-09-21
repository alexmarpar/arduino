import serial
import time
from datetime import datetime

PUERTO = "/dev/ttyACM0"
BAUDRATE = 9600

arduino = serial.Serial(
    PUERTO,
    BAUDRATE,
    timeout=1
)

# Esperar a que el Mega termine de reiniciarse
time.sleep(2)

print("Sending time to Arduino...")

while True:
    hora = datetime.now().strftime("%H:%M")

    arduino.write((hora + "\n").encode())

    print(f"Time sent: {hora}")

    time.sleep(1)