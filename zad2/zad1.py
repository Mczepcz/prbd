import os
import shutil

dir = os.path.join("resources", "lab2", "files")
dirlist = os.listdir(dir)

for filename in dirlist:
    filepath = dir + os.sep + filename
    with open(filepath, "r") as file:
        for line, sentence in enumerate(file, 1):
            newDir = ''
            if line == 1:
                newDir = sentence.split(" ")[1]
                newDirPath = dir+os.sep+newDir
                if not(os.path.exists(newDirPath)):
                    os.makedirs(newDirPath, 0o777)
                shutil.copy(filepath, newDirPath+os.sep+filename)
                break
