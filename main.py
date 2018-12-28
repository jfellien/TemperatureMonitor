from PIL import ImageFont
from datetime import datetime

import os, sys, time

import EPD.epdAPI as EPD

FONT_PATH      = './EPD/fonts/DroidSans.ttf'
FONT_BIG       = ImageFont.truetype(FONT_PATH, 72)
FONT_SMALL     = ImageFont.truetype(FONT_PATH, 12)

BLACK = 0

epd = EPD.EPScreen('landscape')

def get_time():
        full_time = datetime.now().time()
        short_time = str(full_time.hour) + ':' + str(full_time.minute)
        
        return(short_time)

def show_temperature(temperature):
        title = 'Temperatur um ' + get_time() + ':'
        temperature_value = str(temperature) + "°C"

        epd.set_title(title)

        epd.add_text_middle(60, temperature_value, FONT_BIG, BLACK)

        epd.update_screen()

        print(title)
        print(temperature)

def get_current_temperature():
        file = open('/sys/bus/w1/devices/28-01d54c07010c/w1_slave')
        filecontent = file.read()
        file.close()

        stringvalue = filecontent.split("\n")[1].split(" ")[9]
        temperature = float(stringvalue[2:]) / 1000

        rueckgabewert = '%6.1f' % temperature 
        return(rueckgabewert)


temperature = get_current_temperature()
show_temperature(temperature)