import os
import argparse


def listDir(dir):
    """

    :param dir: Path to dir
    :return: List of file
    """
    dir = os.path.join(dir)
    print(dir)
    fileNames = os.listdir(dir)
    for fileName in fileNames:
        print('File Name: ' + fileName)
    return fileNames

def arguments_parsing():
    """

    :return:
    """


    parser = argparse.ArgumentParser(description='files path')
    parser.add_argument("--path", required=True,
                        help="display a path to the directory")

    args = parser.parse_args()
    print(args)
    return args

def file_helper():
    """

    :return:
    """
    args = arguments_parsing()
    print(args.path)
    listDir(args.path)

if __name__ == '__main__':
    file_helper()