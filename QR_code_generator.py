#create a function that collects a text and conver it to a qrcode
#save the qrcode as an image
#install all library
#The command "pip install qrcode Image" 
#installs two Python packages: 
#qrcode and Pillow (formerly known as Image)

import qrcode
from PIL import Image
def QR_Code_generator(data):
    #Create a QR Code instances
    qr=qrcode.QRCode(

        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4
    )
    #Add the data to the QR code
    qr.add_data(data)
    #Generate the QR code
    qr.make(fit=True)
    #crate an image from the QR code
    img=qr.make_image(fill_color="black",black_color="white")
    #save the image
    img.save("qr_code.png")
    img.show()
user_input=input("enter data you want to encode in the QR code: ")
QR_Code_generator(user_input)