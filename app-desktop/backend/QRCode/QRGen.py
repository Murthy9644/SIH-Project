import qrcode, json

class QRGenerator:

    def generator(self):
        qrcode.make(json.dumps(self.data)).save("app-desktop/backend/QRCode/TIDqr.png")

    def __init__(self, data):
        self.data = data
        self.generator()