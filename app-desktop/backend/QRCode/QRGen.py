import qrcode, json, os

class QRGenerator:

    def generator(self):
        code = qrcode.make(json.dumps(self.data))
        code.save(self.qrPath)

    def __init__(self, data):
        self.data = data
        self.qrPath = os.path.normpath(os.path.join(os.getenv("APPDATA"), "Trip Pilot", "QRCodes"))
        os.makedirs(self.qrPath, exist_ok=True)
        self.qrPath = os.path.normpath(os.path.join(self.qrPath, f"{self.data["tid"]}.png"))
        self.generator()