from VES_API import VES
from Camera import Camera
from Tokens import VES_Token, Webhook
from OCR import OCR
import re
import requests

# Use OCR to detect number plate, then
# fetch the API to get the tax status.

camera = Camera()
renderer = OCR()
API = VES(VES_Token)
print("Started")
prev_num = ""
while True:
    try:
        text = renderer.get_text_from_image(camera.get_image())
        print(text)
        import random
        print("Copying file...")
        E = str(random.randint(0, 123123123))
        import os
        os.system("cp '/home/pi/Reg Checker/Test.jpg' '/home/pi/Reg Checker" +
                  "/Cars/Rand" + E + ".jpg'")
        os.system("cp '/home/pi/Reg Checker/Result.jpg' " +
                  "'/home/pi/Reg Checker/Cars/RandRESULT" + E + ".jpg'")
    except Exception as e:
        print(e)
    try:
        num = re.search('[0-9A-Z]{4} [A-Z]{3}', text).group(0)
        print("Num FOUND\n\n\n")
        print(num)
        if num != prev_num:
            print("Finding plate info")
            plate_info = API.check_plate(num.replace(" ", ""))
            import os
            import random
            print("Copying file...")
            E = str(random.randint(0, 123123123))
            os.system("cp '/home/pi/Reg Checker/Test.jpg' '/home/pi/Reg " +
                      "Checker/Cars/Rand" + E + ".jpg'")

            webhook = Webhook
            data = {
                "content": "Vehicle Data Found!!!\n\n" + str(plate_info)
            }
            requests.post(webhook, data=data)
        prev_num = num
    except Exception as e:
        print(e)
        print("No numberplate found.")
