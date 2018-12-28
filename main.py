from PIL import ImageFont

import EPD.epdAPI

FONT_PATH      = './font/FreeMonoBold.ttf'
FONT_BIG       = ImageFont.truetype(FONT_PATH, 72)

BLACK = 0

eps = epsimplelib.EPScreen('landscape')

def show_temperature(temperature):
        eps.set_title("Aktuelle Temperatur")

        eps.add_text_middle(60, str(temperature) + " °C", FONT_BIG, BLACK)

        eps.update_screen()

def get_current_temperature():
        return 45

temperature = get_current_temperature()
show_temperature(temperature)