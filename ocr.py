#!/usr/bin/python3

import pytesseract
from PIL import Image

print(pytesseract.image_to_string(Image.open("./scrape/sap.jpg")))

# TODO create alternative picture with everything below 240/256 black, invert colors
# compare results to vanilla tesseract. use openCV? lookup tables?

# sap_image = Image.open("./scrape/sap.jpg")
# converted_image = sap_image.convert(mode="1", dither=NONE)
# 