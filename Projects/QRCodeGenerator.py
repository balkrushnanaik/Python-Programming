import qrcode

url = input("Enter URL here: ")
filename = input("Enter filename to save the QR code: ")

img = qrcode.make(url)
img.save(filename + ".png")

