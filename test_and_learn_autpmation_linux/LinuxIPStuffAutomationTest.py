import os,re,math, subprocess, datetime



def main():
    os_type = os.name
    file_name = input('if you want to have an output file enter an absolute path here: ')
    ip_list_all_nic = ip_grab_list(os_type)
    ip_loop_output(ip_list_all_nic,file_name)


def ip_grab_list(os_type):

    if os_type == 'posix':
        ip_var = subprocess.run(['ifconfig', '-a'], capture_output=True).stdout.decode()
    elif os_type == 'nt':
        ip_var = subprocess.run(["ipconfig", '/all'], capture_output=True).stdout.decode()
        print(ip_var)
    find_target_ip_regex_object = re.compile(r'\d{1,3}[.]\d{1,3}[.]\d{1,3}[.]\d{1,3}')
    ip_regex_o = re.compile(r'inet\s\d{1,3}[.]\d{1,3}[.]\d{1,3}[.]\d{1,3}')
    ip_regex_o_search = ip_regex_o.findall(ip_var)
    search_join= ''.join(ip_regex_o_search)
    ip_regex_o_search_f = find_target_ip_regex_object.findall(search_join)
    print(ip_var)
    return ip_regex_o_search_f


def file_check(file_name):
    if file_name == '' and os.path.exists('./log_file') is not True or os.path.getsize('./log_file') == 0:
        file = open('log_file', 'w')
        return file
    if file_name == '' and os.path.exists('./log_file') is True or os.path.getsize('./log_file') != 0:
        file = open('log_file', 'a')
        return file
    elif os.path.exists(file_name) is not True or os.path.getsize(file_name) == 0:
        file = open(file_name, 'w')
        return file
    else:
        file = open(file_name, 'a')
        return file


def ip_loop_output(ip_list,file_name):
    temp_file = file_check(file_name)
    for item in ip_list:
        ping_output = subprocess.run(["ping", "-c", "3", item],capture_output=True).stdout.decode()
        print(ping_output)
        if temp_file != 'none':
            temp_file.write(f'IP address is:\n{item}\n\nping output:\n{ping_output}\ncompleated: {datetime.datetime.now()}\n\n')


if __name__ == '__main__':
    main()
