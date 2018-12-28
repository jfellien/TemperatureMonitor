from PIL import ImageFont

import EPD.epdAPI as EPD

FONT_PATH      = './EPD/fonts/DroidSans.ttf'
FONT_BIG       = ImageFont.truetype(FONT_PATH, 72)

BLACK = 0

epd = EPD.EPScreen('landscape')

def show_temperature(temperature):
        epd.set_title("Aktuelle Temperatur")

        epd.add_text_middle(60, str(temperature) + " °C", FONT_BIG, BLACK)

        epd.update_screen()

def get_current_temperature():
        return 45

temperature = get_current_temperature()
show_temperature(temperature)