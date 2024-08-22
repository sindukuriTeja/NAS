import Adafruit_DHT
from RPLCD.i2c import CharLCD
from time import sleep

# Sensor type and pin configuration
DHT_SENSOR = Adafruit_DHT.DHT11
DHT_PIN = 4  # GPIO pin where the DHT11 is connected

# LCD configuration
lcd = CharLCD(i2c_expander='PCF8574', address=0x27, port=1,
              cols=16, rows=2, dotsize=8,
              charmap='A00', auto_linebreaks=True,
              backlight_enabled=True)

def read_temperature():
    humidity, temperature = Adafruit_DHT.read(DHT_SENSOR, DHT_PIN)
    if humidity is not None and temperature is not None:
        return temperature, humidity
    else:
        return None, None

def display_on_lcd(temperature, humidity):
    lcd.clear()
    if temperature is not None and humidity is not None:
        lcd.write_string(f'Temp: {temperature:.1f}C')
        lcd.crlf()
        lcd.write_string(f'Hum: {humidity:.1f}%')
    else:
        lcd.write_string("Sensor error")

if _name_ == "_main_":
    while True:
        temp, hum = read_temperature()
        display_on_lcd(temp, hum)
        sleep(2)