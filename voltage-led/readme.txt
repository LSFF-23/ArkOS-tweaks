sudo nano /usr/local/bin/voltage_led_warning.py
sudo chmod +x /usr/local/bin/voltage_led_warning.py
sudo nano /etc/systemd/system/voltage-led.service
sudo systemctl daemon-reload
sudo systemctl enable voltage-led
sudo systemctl start voltage-led
sudo systemctl status voltage-led

darkos-re has its own battery/led manager:
sudo nano /usr/local/bin/batt_life_warning.py
sudo systemctl restart batt_led.service

since its battery driver is already adapting to poor battery condition, i've only disabled the annoying blue led when battery isn't low:
...
  if cap >= 30:
    blue_off()
...