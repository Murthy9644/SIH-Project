import webview, sys
from screeninfo import get_monitors
from ui.stylesheet import sheet
from ui.utils.Utils import widUtils
from backend.dataTransfer import DataTransfer
from server_config.findServer import FindServer

class TripPilot:

    def __init__(self):

        try:
            self.server = FindServer()
            self.serverIP = self.server.serverIPCopy

        except AttributeError as e:
            print(e, '\n', "Couldn't connect to the server. Check your connection")
            sys.exit()

        self.dataTransfer = DataTransfer(self.serverIP)
        self.widutils = widUtils(self.serverIP)


api = TripPilot()

monitor = get_monitors()[0]
screenWidth, screenHeight = monitor.width, monitor.height

webview.create_window(
    "TripPilot",
    html = sheet,
    js_api = api,
    height= int(screenHeight * 0.7),
    width= int(screenWidth * 0.6),
    resizable= False,
    fullscreen = True
)

webview.start()