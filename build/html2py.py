import os, sys

class Paths:

    def __init__(self):
        self.rootDir = os.path.normpath(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        self.folderPath = os.path.normpath(os.path.join(self.rootDir, "front-end"))
        self.html = os.path.normpath(os.path.join(self.folderPath, "index.html"))
        self.css = os.path.normpath(os.path.join(self.folderPath, "style.css"))
        self.js = os.path.normpath(os.path.join(self.folderPath, "script.js"))

class Converter:

    def loadFiles(self):
        with open(self.paths.html, 'r') as index: self.htmlLines = index.readlines()
        with open(self.paths.css, 'r') as style: self.cssLines = style.readlines()
        with open(self.paths.js, 'r') as script: self.jsLines = script.readlines()

    def setupCode(self):
        styleTag = "\t<style>\n"
        for i in self.cssLines: styleTag += '\t\t' + i
        styleTag += "\n\t</style>"

        scriptTag = "\t<script>\n"
        for i in self.jsLines: scriptTag += '\t\t' + i
        scriptTag += "\n\t</script>\n"

        self.htmlLines = [styleTag if x.strip() == '<link rel="stylesheet" href="style.css">' else x for x in self.htmlLines]
        self.htmlLines = [scriptTag if x.strip() == '<script src="script.js"></script>' else x for x in self.htmlLines]

        self.htmlLines.insert(0, "sheet = '''\n")
        self.htmlLines.append("\n'''")

    def writeCode(self):

        try:
            if sys.argv[1] == '-d':
                basePath = os.path.normpath(os.path.join(self.paths.rootDir, "app-desktop"))

            elif sys.argv[1] == '-m':
                basePath = os.path.normpath(os.path.join(self.paths.rootDir, "app-mobile"))
            
            else: raise(Exception)

        except:
            print("option not specified-compilation is terminated.")
            sys.exit()

        filePath = os.path.normpath(os.path.join(basePath, "ui", "stylesheet.py"))
        
        with open(filePath, 'w') as file: file.writelines(self.htmlLines)

    def __init__(self):
        self.paths = Paths()
        self.loadFiles()
        self.setupCode()
        self.writeCode()

Converter()