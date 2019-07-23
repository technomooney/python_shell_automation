import subprocess,re
def setup(): #this is for installing the required module for when a user just open the py file in explorer and tell the user they need python 3.7>=
    if os.path.exists('./do.not.delete.done_setup.log') is False:
        version = subprocess.run(['python','--version'],capture_output=True).stdout.decode()
        ver_reg = re.compile(r'([3-9].\d)')
        version_num = float(re.search(ver_reg,version).group(1))
        required_version = 3.7
        if version_num < required_version:
            nice_quit(err=f'found a python version lower then the accepted version of {required_version} or higher: {version}')

        output = subprocess.run(['pip','install','--user','xlsxwriter'],capture_output=True).stdout.decode()
        out= open('do.not.delete.done_setup.log','w')
        out.write(output)
        input(f'setup needed to be done, i installed xlsxwriter to use for this program... the file called \'do.not.del'
              f'ete.done_setup\' \nis there to tell thss proggram the setup was done already and theere is no need to do'
              f'it again! do not remove it unless \nyou want to rthe setup function again... \n\n press enter to conttinue')


try:
    import os,glob,datetime,xlsxwriter,time
except ModuleNotFoundError as err:
    print(err)
    setup()


def main():
    setup()
    path = get_paths()
    globs= win_files(path)
    data = make_file_attri_dict(globs)
    save_xls(path,data)
    restart = input('\n\ndo you want to do another directory? to exit press \'n\' otherwise just press enter: ').lower()
    if restart != 'n':
        main()
    else:
        nice_quit()


def win_files(path):
    file_globs = glob.glob(path+r'\**\*',recursive=True)
    return file_globs

def save_xls(path,data):
    path_append= str(os.path.expanduser('~'))+r'\Documents\.'
    filename= path_append+str(path).replace("\\",'_').replace(':','')+f"---{str(datetime.datetime.now()).replace(':','..')}.xlsx"
    print(f'the file will be saved in {path_append}')

    wb = xlsxwriter.Workbook(filename)
    worksheet = wb.add_worksheet('Files and attributes')
    number= wb.add_format({'num_format':'#,##0.###'})
    worksheet.set_column(0,10,30)
    row = 0
    col = 0
    for (file,filedata) in data.items():
        temp= col+1
        worksheet.write(row,col,file)
        for item in filedata:
            worksheet.write(row,temp,item,number)
            temp += 1
        row += 1
    wb.close()

def get_paths():
    path=input('enter the path you want to index into an excel file: ')
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
    data['file name'] = ['file path','file size in MB','last access time','Creation time']
    try:
        for item in globbed_files:
            data[os.path.basename(item)] = [item,(os.stat(item).st_size/1024)/1024, str(datetime.datetime.fromtimestamp(os.stat(item).st_atime)),str(datetime.datetime.fromtimestamp(os.stat(item).st_ctime))]
    except Exception as err:
        print(err)
        print('\nwe found a path/location that you dont have access or the system cant find\n')

    return data

def nice_quit(err=None):
    if err !=None:
        print(err)
        print('Sorry for any inconvenience.')
    print('thanks for using the program made by Mary Mooney')
    time.sleep(5)
    quit()


main()

# todo: make an empty folder sheet
# todo: make it look nicer....


