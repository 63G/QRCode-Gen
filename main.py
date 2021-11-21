import time
import random
import qrcode
from PIL import Image


def imgcreator(link1):
    link1 = link1
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(link1)
    img = qr.make()



# QRCODECREATOR
print("Hello there!")
time.sleep(1)
t = 1
c = input('Do you want to make a QRImage? Y/N')
if c.lower() == 'y':
    print("Great!")
    link = input("Link? ")
    print(link)
    img = qrcode.make(link)
    type(img)
    logo_display = Image.open("profiler.jpeg")
    logo_display.thumbnail((60, 60))
    logo_pos = ((img.size[0] - logo_display.size[0]) // 2, (img.size[1] - logo_display.size[1]) // 2)
    img.paste(logo_display, logo_pos)
    imgcreator(link)
    filename = str(random.randint(1, 100000000))
    img.save(filename + ".png")
    print("Check Files ;)")
elif c.lower() == 'n':
    print("Alright See you")
    exit()
else:
    print("Can't really process this answer")


