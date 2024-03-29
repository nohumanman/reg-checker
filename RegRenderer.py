from ast import Pass
from xml.dom.minidom import Attr
import pytesseract
from pkg_resources import get_importer
from VES import VES
import cv2
import re
import numpy as np
import time
from PIL import Image, ImageOps


class RegRenderer():
    def __init__(self):
        pass
        # self.camera = PiCamera()
        # self.camera.start_preview()

    def wait_for_plate(self):
        text = self.get_text_from_image(
            self.get_image()
        )
        num = re.search('[0-9A-Z]{4} [A-Z]{3}', text).group(0)
        return num

    def get_image(self):
        # self.camera.capture('Capture.png')
        return "Capture.png"

    def get_text_from_image(self, directory: str):
        pytesseract.pytesseract.tesseract_cmd = (
            "C:\\Program Files\\" +
            "Tesseract-OCR\\tesseract.exe"
        )
        image = cv2.imread(directory)
        original = image.copy()
        image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
        lower = np.array([15, 50, 50], dtype="uint8")
        upper = np.array([30, 255, 255], dtype="uint8")
        mask = cv2.inRange(image, lower, upper)
        cnts = cv2.findContours(
            mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        cnts = cnts[0] if len(cnts) == 2 else cnts[1]
        cv2.fillPoly(mask, cnts, (255, 255, 255))
        result = cv2.bitwise_and(original, original, mask=mask)
        result = cv2.cvtColor(result, cv2.COLOR_BGR2GRAY)
        thresh, blackAndWhiteImage = cv2.threshold(result, 127, 255,
                                                   cv2.THRESH_BINARY)
        cnts = cv2.findContours(blackAndWhiteImage, cv2.RETR_EXTERNAL,
                                cv2.CHAIN_APPROX_SIMPLE)[-2]
        cnt = sorted(cnts, key=cv2.contourArea)[-1]
        x, y, w, h = cv2.boundingRect(cnt)
        dst = blackAndWhiteImage[y:y+h, x:x+w]
        cv2.imwrite("Result.jpg", dst)
        rendered_text = (pytesseract.image_to_string(
                        ImageOps.grayscale(Image.open("Result.jpg")),
                        lang="eng", config="--psm 7"
            ))
        rendered_text = rendered_text.replace("\u000C", "")
        rendered_text = rendered_text.replace("\n", "")
        rendered_text = rendered_text.replace("-", "")
        rendered_text = rendered_text.replace("|", "")
        rendered_text = rendered_text.replace(",", "")
        rendered_text = rendered_text.replace(".", "")
        return rendered_text
