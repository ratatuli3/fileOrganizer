import os
import time


def monitorDownloads(directory):
    while True:
        Files = set(os.listdir(directory))
        for fileName in Files:
            dotIndex = fileName.rfind('.')
            filePath = directory+"/"+fileName
            fileDirectory = "/home/skibidi/Videos/" + (fileName[dotIndex+1:]).upper()
            fileDestination = fileDirectory+"/"+fileName
            os.makedirs(fileDirectory, exist_ok=True)
            os.rename(filePath, fileDestination)
        time.sleep(5)


if __name__ == "__main__":
    downloadsDirectory = "/home/skibidi/Downloads"
    monitorDownloads(downloadsDirectory)