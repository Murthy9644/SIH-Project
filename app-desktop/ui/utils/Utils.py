import requests, json

class AsyncUtils:

    def getTouristsNdetails(self):
        response = requests.get("http://172.20.113.56:5500/getTouristData/all")
        print(response.text)

        if response.text == "null": return "null"

        return response.text


class widUtils:

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
    
    def getServerIP(self):
        return self.serverIP
    
    def __init__(self, serverIP):
        self.serverIP = serverIP