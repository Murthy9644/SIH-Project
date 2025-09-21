from .QRCode.QRGen import QRGenerator
import requests

class DataTransfer:

    def sendData(self, data, tid):
        self.details = {
            "tid": tid, 
            "data": data
        }

        dataResponse = requests.post(self.serverIP + f"/write/touristData.json", json = self.details)
        self.qrGenInst = QRGenerator(self.details)
        self.qrPath = self.qrGenInst.qrPath
        qrResponse = self.sendQR()

        return [dataResponse.text, qrResponse]

    def sendQR(self):

        try:
            with open(self.qrPath, 'rb') as image: 
                response = requests.post(self.serverIP + f"/upload/{self.details["tid"]}.png", files = {"image": image})
                print(response.text)

            return response.text

        except Exception as e:
            response = "QR-upload-failed"
            print(response, e)
            
            return response
        
    def getLoginInfo(self, id):
        response = requests.get(f"{self.serverIP}/getLoginInfo/{id}")

        return response.json()
    
    def __init__(self, serverIP):
        self.serverIP = serverIP