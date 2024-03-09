import os
import time


def monitorDownloads(directory):
    while True:
        Files = set(os.listdir(directory))
        for fileName in Files:
            dotIndex = fileName.rfind('.')
            filePath = os.path.join(directory, fileName)
            fileDirectory = os.path.join("C:\\Destination\\Directory\\Path\\Here", (fileName[dotIndex+1:]).upper())
            fileDestination = os.path.join(fileDirectory, fileName)
            os.makedirs(fileDirectory, exist_ok=True)
            os.rename(filePath, fileDestination)
        time.sleep(5)


if __name__ == "__main__":
    downloadsDirectory = "C:\\Full\\Path\\Here"
    monitorDownloads(downloadsDirectory)
