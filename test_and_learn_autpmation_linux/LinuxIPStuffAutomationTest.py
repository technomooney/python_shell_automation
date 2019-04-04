import os,re,math, subprocess



def main():
    file_name = input('if you want to have an output file enter an absolute path here: ')
    ip_list_all_nic = ip_grab_list()
    ip_loop_output(ip_list_all_nic,file_name)
def ip_grab_list():
    ifconfig_var = subprocess.check_output(['ifconfig', '-a']).decode()#grabbing the ip address from the ifconfig comand
    # print(str(ifconfig_var))
    find_target_ip_regex_object = re.compile(r'\d{1,3}[.]\d{1,3}[.]\d{1,3}[.]\d{1,3}')
    ip_regex_o = re.compile(r'inet\s\d{1,3}[.]\d{1,3}[.]\d{1,3}[.]\d{1,3}')
    ip_regex_o_search = ip_regex_o.findall(ifconfig_var)
    search_join= ''.join(ip_regex_o_search)
    ip_regex_o_search_f = find_target_ip_regex_object.findall(search_join)
    # print(ifconfig_var) ''' you didnt lock you PC   ;)))))))))
    return ip_regex_o_search_f


def file_check(file_name):

    if file_name == '':
        return 'none'
    elif os.path.exists(file_name) is not True or os.path.getsize(file_name) == 0:
        file = open(file_name, 'w')
        return file
    else:
        file = open(file_name, 'a')
        return file


def ip_loop_output(ip_list,file_name):
    temp_file = file_check(file_name)
    for item in ip_list:
        ping_output = subprocess.check_output(["ping", "-c", "3", item]).decode()
        print(ping_output)
        if temp_file == 'none':
            temp_file.write(f'IP address is:\n{item}\n\nping output:\n{ping_output}\n\n')
    file_name.close() # close the file opened by file_check()

if __name__ == '__main__':
    main()
