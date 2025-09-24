import webview, sys
from ui.stylesheet import sheet
from ui.utils.Utils import widUtils, AsyncUtils
from backend.dataTransfer import DataTransfer
from server_config.findServer import FindServer

class TripPilot:

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


api = TripPilot()

webview.create_window(
    "TripPilot",
    html = sheet,
    js_api = api,
    resizable= False,
    fullscreen = True
)

webview.start()