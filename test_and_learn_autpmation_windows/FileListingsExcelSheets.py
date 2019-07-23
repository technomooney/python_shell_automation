import os,glob,datetime,xlsxwriter,subprocess


def main():
    setup()
    path = get_paths()
    globs= win_files(path)
    data = make_file_attri_dict(globs)
    # for (filename,filedata) in data.items():
    #     print(filename)
    #     print(filedata)
    save_xls(path,data)



def setup():
    if os.path.exists('./do.not.delete.done_setup') is False:
        output = subprocess.run(['python','pip','install','--user','xlsxwriter'],capture_output=True).stdout.decode()
        out= open('do.not.delete.done_setup','w')
        out.write(output)
        input('setup needed to be done, i installed xlsxwriter to use for this program... the file called \'do.not.del'
              'ete.done_setup\' \nis there to tell thss proggram the setup was done already and theere is no need to do '
              'it again! do not remove it unless \nyou want to rthe setup function again... \n\n press enter to conttinue')

def win_files(path):
    file_globs = glob.glob(path+r'\**\*',recursive=True)
    return file_globs

def save_xls(path,data):
    filename= str(path).replace("\\",'_').replace(':','')+f"---{str(datetime.datetime.now()).replace(':','..')}.xlsx"

    wb = xlsxwriter.Workbook(filename)
    worksheet = wb.add_worksheet('Files and attributes')
    number= wb.add_format({'num_format':'#,##0.###'})
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
    for item in globbed_files:
        data[os.path.basename(item)] = [item,(os.stat(item).st_size/1024)/1024, str(datetime.datetime.fromtimestamp(os.stat(item).st_atime)),str(datetime.datetime.fromtimestamp(os.stat(item).st_ctime))]
    return data


main()

# todo: make an empty filder sheet
# todo: make it look nicer....


