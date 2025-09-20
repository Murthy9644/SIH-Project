import socket, requests, threading

class FindServer:
    port = 5500

    def getIPV4(self):
        print("Getting ipv4 address...")
        socky = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        try:
            socky.connect(("8.8.8.8", 80))
            ip = socky.getsockname()[0]

        finally: socky.close()

        print(f"ipv4 address:{ip}")

        return ip

    def getSubNet(self):
        self.subNet, self.deviceIP = self.ip.rsplit('.', 1)
        self.subNet = "http://" + self.subNet
        print("Sub net of this network: ", self.subNet)

    def findServer(self, start, end):

        for i in range(start, end):
            
            if self.found: break

            ipAdd = self.subNet + '.' + str(i) + ':' + str(self.port)
            print("Checking server for ", ipAdd)

            try:
                request = requests.get(ipAdd + "/confirm", timeout=0.5)
                print(request.text)
                
                if request.text == "confirm-listening on port 5500":
                    self.serverIP = ipAdd
                    self.serverIPCopy = self.serverIP
                    print("Server Found!")
                    self.found = True
                    break

            except requests.exceptions.RequestException:
                self.serverIP = None
                continue

        if not self.serverIP and not self.found: print("Server not found")

    def startFinding(self):
        threads, start, end = [], 1, 26

        for i in range(0, 10):
            t = threading.Thread(target=self.findServer, args = (start, end))
            threads.append(t)
            t.start()
            start, end = start + 25, end + 25

        t = threading.Thread(target=self.findServer, args = (start, 255))
        threads.append(t)
        t.start()

        for thread in threads: thread.join()
    
    def __init__(self):
        self.found = False
        print("Starting process...")
        self.ip = self.getIPV4()
        self.getSubNet()
        self.startFinding()

if __name__ == "__main__":
    server = FindServer()
    print(server.serverIPCopy)