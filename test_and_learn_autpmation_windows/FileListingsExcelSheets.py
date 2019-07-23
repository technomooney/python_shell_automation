import os,subprocess,re,glob,datetime

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
    print(walk_var)
    glob_var=glob.glob(path + r'\**\*', recursive=True)
    print(glob_var)
    for item in glob_var:
        print(datetime.datetime.fromtimestamp(os.stat(item).st_atime), os.stat(item).st_size)
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