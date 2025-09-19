from .QRCode.QRGen import QRGenerator
import requests

class DataTransfer:

    def getIPV4(self):
        import socket

        socky = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        try:
            socky.connect(("8.8.8.8", 80))
            ip = socky.getsockname()[0]

        finally: socky.close()

        return ip

    def sendData(self, data, tid):
        details = {
            "tid": tid, 
            "data": data
        }

        response = requests.post(self.url + f"/write/touristData.json", json = details)
        QRGenerator(details)

        return response.text
    
    def __init__(self):
        self.url = f"http://{self.getIPV4()}:5500"