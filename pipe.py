import os, sys

try:
    match sys.argv[1]:
        case "-dm": os.system("python app-desktop/Main.py")
        case "-mm": os.system("python app-mobile/Main.py")
        case "-dc": os.system('python build/html2py.py -d')
        case "-mc": os.system('python build/html2py.py -m')
        case _: raise(Exception)
            
except:   
    print('''unrecognized command:
          
    Structure - 'pipe.py -command'
          
commands <
    '-dm' = Run Main.py under app-desktop
    '-mm' = Run Main.py under app-mobile
    '-dc' = Compile the .html, .css, .js into app-desktop
    '-mc' = Compile the .html, .css, .js into app-mobile
>'''
)