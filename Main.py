from VES import VES
from Tokens import VES_Token
from RegRenderer import RegRenderer

reg_renderer = RegRenderer()
ves_api = VES(VES_Token)

prev_num = ""

while True:
   plate = reg_renderer.wait_for_plate()
   print("Plate found! '" + plate + "'")
   info = ves_api.check_plate(plate)
   print("Info found on plate - '" + info + "'")

