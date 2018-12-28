from PIL import ImageFont
from datetime import datetime

import os, sys, time

import EPD.epdAPI as EPD

FONT_PATH      = './EPD/fonts/DroidSans.ttf'
FONT_BIG       = ImageFont.truetype(FONT_PATH, 72)
FONT_SMALL     = ImageFont.truetype(FONT_PATH, 12)

BLACK = 0

epd = EPD.EPScreen('landscape')

def show_temperature(temperature):
        epd.set_title("Aktuelle Temperatur")

        epd.add_text_middle(60, str(temperature) + " °C", FONT_BIG, BLACK)

        epd.add_text_middle(140, datetime.now().time(), FONT_SMALL, BLACK)

        epd.update_screen()

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