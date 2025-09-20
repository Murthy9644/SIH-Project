import webview
from ui.stylesheet import sheet

webview.create_window(
    "TripPilot",
    html = sheet,
    resizable= False,
    fullscreen = True
)