import webview
from ui.stylesheet import sheet
from ui.utils.Utils import WidUtils, AsyncUtils
from backend.dataTransfer import DataTransfer

class TripPilot:

    def getInstances(self):
        self.widutils = WidUtils()
        self.serverIP = self.widutils.serverIP
        self.dataTransfer = DataTransfer(self.serverIP)
        self.asyncutils = AsyncUtils()


api = TripPilot()

webview.create_window(
    "TripPilot",
    html = sheet,
    js_api = api,
    resizable= False,
    fullscreen = True
)

webview.start()