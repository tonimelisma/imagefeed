# imagefeed - an algorithmic feed of funny images

Imagefeed takes the popular image sharing site imgur where entertaining pictures
are shown in a random order, classifies the pictures (based on text contained
in them as well what's in the image), clusters images based on content and shows
the user images tailored to their liking.

Tools used:
- Python
- imgur-scraper for scraping images
- tinydb for JSON database
- Tesseract for OCR
- Keras and Tensorflow for image classification