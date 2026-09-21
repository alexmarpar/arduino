after that create the service:
sudo nano /etc/systemd/system/arduino-clock.service

```
[Unit]
Description=Reloj Arduino
After=network.target

[Service]
Type=simple
User=alex
WorkingDirectory=/home/alex/reloj
ExecStart=/home/alex/arduino/clock/venv/bin/python /home/alex/arduino/clock/clock.py
Restart=always
RestartSec=5

[Install]
WantedBy=multi-user.target
```
sudo systemctl daemon-reload
sudo systemctl enable --now arduino-clock.service

logs:
```
journalctl -u reloj-arduino.service -f
```