import requests, os

try:
    with open(os.path.normpath("F:\\Desktop\\SIH-Project\\.assets\\Trip-Pilot-Logo.png"), 'rb') as file:
        response = requests.post("http://172.20.113.56:5500/uploadLogo", files= {"image":file},timeout=10)
        print(response.text)    

except Exception as e: print(e)

except requests.exceptions.RequestException as e: print(e)
