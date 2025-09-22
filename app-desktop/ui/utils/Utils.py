from server_config.findServer import FindServer
import sys

class AsyncUtils:

    def closeExe(self):
        sys.exit()

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