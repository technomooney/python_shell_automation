import os,subprocess,re

def main():
    path = get_paths()
    test(path)
    # win_dir(path)

def win_dir(path):

    type(os.walk(path))
    for root, dirs, files in os.walk(path):

        print(dict)


def test(path):

    walk_var = list(os.walk(path))
    # for item in walk_var:
    #     print(item)
    i0 = walk_var[0]
    print(i0)
    i1 = walk_var[1]
    print(i1)
    i3 = walk_var[3]
    print(i3)
    i4 = walk_var[4]
    print(i4)
    i5 = walk_var[5]
    print(i5)
    i6 = walk_var[6]
    print(i6)
    i7 = walk_var[7]
    print(i7)
    i8 = walk_var[8]
    print(i8)
    i9 = walk_var[9]
    print(i9)

def get_paths():
    path=input('enter the path: ')
    path = path_check(path , check=1)
    return path


def path_check(path,check=None):
    if os.path.exists(path):
        print('ok')
    elif check is not None and os.path.exists(path) is False:
        while os.path.exists(path) is False:
            path = input(f'that path \"{path}\" does not exist, try again: ')
    return path

def file_listings(directory):
    print()

main()