class widUtils:

    def credCheck(self, data, screen):

        match screen:
            case "loginScreen":

                for key, value in data.items():
                    
                    if value == '': return False
                    
            case "detailsScreen":

                for key, value in data.items():
                    
                    if value == '': return False

        return True
    
    def getServerIP(self):
        return self.serverIP
    
    def __init__(self, serverIP):
        self.serverIP = serverIP