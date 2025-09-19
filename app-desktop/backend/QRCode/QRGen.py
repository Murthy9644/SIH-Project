import qrcode, json

class QRGenerator:

    def generator(self):
        code = qrcode.make(json.dumps(self.data))
        code.save(f"app-desktop/backend/QRCode/{self.data["tid"]}.png")

    def __init__(self, data):
        self.data = data
        self.generator()