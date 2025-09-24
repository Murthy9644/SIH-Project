<<<<<<< HEAD
import requests, json

class AsyncUtils:

    def getTouristsNdetails(self):
        response = requests.get("http://172.20.113.56:5500/getTouristData/all")
        print(response.text)

        if response.text == "null": return "null"

        return response.text


class widUtils:
=======
from server_config.findServer import FindServer
import sys

class AsyncUtils:

    def closeExe(self):
        sys.exit()
>>>>>>> 72871a44a6e2e1638e54fd1e4aefe3dcbfda5b99

    def printer(self, text): print(text)

    def credCheck(self, data, screen):

        match screen:
            case "loginScreen":

                for key, value in data.items():
                    
                    if value == '': return False
                    
            case "detailsScreen":

                for key, value in data.items():
                    
                    if value == '': return False

        return True

class WidUtils:
    
    def getServerIP(self):
        return self.serverIP
    
    def setServerIP(self):
        
        try:
            self.server = FindServer()

            return self.server.serverIPCopy

        except AttributeError as e:
            print(e, '\n', "Couldn't connect to the server. Check your connection")
            
            return 0
    
    def __init__(self):
        self.serverIP = self.getServerIP()