from PIL import ImageFont
from datetime import datetime
from w1thermsensor import W1ThermSensor

import os, sys, time

import EPD.epdAPI as EPD

FONT_PATH      = './EPD/fonts/DroidSans.ttf'
FONT_BIG       = ImageFont.truetype(FONT_PATH, 72)
FONT_SMALL     = ImageFont.truetype(FONT_PATH, 12)

BLACK = 0

epd = EPD.EPScreen('landscape')

def get_time():
        full_time = datetime.now().time()
        hour = str(full_time.hour)
        minute = "{:02d}".format(full_time.minute)
        short_time = hour + ':' + minute
        
        return(short_time)

def get_current_temperature():
        sensor = W1ThermSensor()

        temperature = sensor.get_temperature()
        temperature_formated = "{:3.1f}".format(temperature)

        return(temperature_formated)

def show_temperature():
        temperature = get_current_temperature()

        title = 'Temperatur um ' + get_time()
        temperature_value = str(temperature) + "°C"

        epd.set_title(title)

        epd.add_text_middle(60, temperature_value, FONT_BIG, BLACK)

        epd.update_screen()

        print(title)
        print(temperature)


show_temperature()