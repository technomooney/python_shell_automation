import os,subprocess,re,glob,datetime

def main():
    path = get_paths()
    globs= win_files(path)
    data = make_file_attri_dict(globs)
    for (file,attri_list) in data.items():
        print(file)
        print(attri_list)



def win_files(path):
    file_globs = glob.glob(path+r'\**\*',recursive=True)
    print(file_globs)
    return file_globs


#
# def test(path):
#     glob_var=glob.glob(path + r'\**\*', recursive=True)
#     print(glob_var)
#     for item in glob_var:
#         print(datetime.datetime.fromtimestamp(os.stat(item).st_atime), os.stat(item).st_size)




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

def make_file_attri_dict(globbed_files):
    data={}
    for item in globbed_files:
        data[item] = [(os.stat(item).st_size/1024), str(datetime.datetime.fromtimestamp(os.stat(item).st_atime))]
    return data


main()

# TODO: get openxls or XlsxWriter and test how to make the final file
# todo: be sure to make the file names of the xlsx file based off the time it was run and the path name by replacing
#  the /s with -s

