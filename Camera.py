from picamera import PiCamera


class Camera():
    def __init__(self):
        self.camera = PiCamera()
        self.camera.start_preview()

    def get_image(self):
        self.camera.capture('Test.jpg')
        return "Test.jpg"
