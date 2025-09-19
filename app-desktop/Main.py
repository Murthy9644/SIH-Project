import webview
from screeninfo import get_monitors
from ui.stylesheet import sheet
from ui.utils.Utils import widUtils
from backend.dataTransfer import DataTransfer

class TripPilot:

    def __init__(self):
        self.widutils = widUtils()
        self.dataTransfer = DataTransfer()


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