import json

class DataIO:

    def write(self, path, data):
        with open(path, 'w') as file: json.dump(data, file, indent=4)
        
        return True
    
    def read(self, path):
        with open(path, 'r') as file: data = json.load(file)

        return data