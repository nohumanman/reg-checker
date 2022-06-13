from VES import VES
from Tokens import ves_token
from RegRenderer import RegRenderer

reg_renderer = RegRenderer()
ves_api = VES(ves_token)

prev_num = ""

while True:
    plate = reg_renderer.wait_for_plate()
    if plate != prev_num:
        print("Plate found! '" + plate + "'")
        prev_num = plate
    # info = ves_api.check_plate(plate)
    # print("Info found on plate - '" + info + "'")
