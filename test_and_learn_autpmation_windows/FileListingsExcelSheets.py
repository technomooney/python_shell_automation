import os,subprocess,re

def main():
    get_paths(check = '1')
    get_paths()
    print()


def get_paths(check=None):

    path=input('enter the path: ')
    path = path_check(path,check)
    print(check)
    print(path)


def path_check(path,*check):
    if os.path.exists(path):
        print('ok')
    elif check is not None and os.path.exists(path) is False:
        while os.path.exists(path) is False:
            path = input(f'that path \"{path}\" does not exist, try again: ')
    print(check)
    return path

def file_listings(directory):
    print()

main()