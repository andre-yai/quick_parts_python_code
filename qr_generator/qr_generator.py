# This code generates a qr_code
import pyqrcode
def generator(url_string, png_filename):
    url = pyqrcode.create(url_string)
    url.png(png_filename)

if __name__ == '__main__':
    url_string = "http://google.com"
    png_filename = "google.png"
    generator(url_string,png_filename)
