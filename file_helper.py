import os

Folder_Path = r'D:\\MyWorkFolder'

def listDir(dir):
    fileNames = os.listdir(dir)
    for fileName in fileNames:
        print('File Name: ' + fileName)
        print('Folder Path: ' + os.path.abspath(os.path.join(dir, fileName)), sep='\n')

if __name__ == '__main__':
    listDir(Folder_Path)