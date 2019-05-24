import os
import argparse


def listDir(dir):
    fileNames = os.listdir(dir)
    for fileName in fileNames:
        print('File Name: ' + fileName)
        print('Folder Path: ' + os.path.abspath(os.path.join(dir, fileName)), sep='\n')

def arguments_parsing():

    parser = argparse.ArgumentParser(description='files path')
    parser.add_argument("--path", type="dir_path",
                        help="display a path to the directory")

    args = parser.parse_args()
    return args

def file_helper():
    args = arguments_parsing()
    print(args.path)
    print(listDir)

if __name__ == '__main__':
    file_helper()