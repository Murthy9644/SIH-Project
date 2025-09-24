<<<<<<< HEAD
import webview, sys
from ui.stylesheet import sheet
from ui.utils.Utils import widUtils, AsyncUtils
=======
import webview
from ui.stylesheet import sheet
from ui.utils.Utils import WidUtils, AsyncUtils
>>>>>>> 72871a44a6e2e1638e54fd1e4aefe3dcbfda5b99
from backend.dataTransfer import DataTransfer

class TripPilot:

<<<<<<< HEAD
    def __init__(self):
        # try:
        #     self.server = FindServer()
        #     self.serverIP = self.server.serverIPCopy

        # except AttributeError as e:
        #     print(e, '\n', "Couldn't connect to the server. Check your connection")
        #     sys.exit()

        self.serverIP = "http://172.20.113.56:5500"
        self.dataTransfer = DataTransfer(self.serverIP)
        self.widutils = widUtils(self.serverIP)
        self.asyncUtils = AsyncUtils()
=======
    def getInstances(self):
        self.widutils = WidUtils()
        self.serverIP = self.widutils.serverIP
        self.dataTransfer = DataTransfer(self.serverIP)
        self.asyncutils = AsyncUtils()
>>>>>>> 72871a44a6e2e1638e54fd1e4aefe3dcbfda5b99


api = TripPilot()

webview.create_window(
    "TripPilot",
    html = sheet,
    js_api = api,
    resizable= False,
    fullscreen = True
)

webview.start()