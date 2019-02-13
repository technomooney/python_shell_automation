import os,re,math, subprocess

# ipconfig_var = subprocess.check_output('ifconfig -a', shell=True).decode()
ipconfig_var = subprocess.check_output(f"ipconfig").decode()

print(str(ipconfig_var))

ip_regex_o = re.compile(r'192{1,3}[.]\d{1,3}[.]\d{1,3}[.]\d{1,3}|10[.]\d{1,3}[.]\d{1,3}[.]\d{1,3}')
print(type(ipconfig_var))
ip_regex_o_search = ip_regex_o.findall(ipconfig_var)
print(type(ipconfig_var))
print(ipconfig_var)
print(ip_regex_o_search)

if os.path.exists(r'C:\Users\Marty Mooney\Desktop\program_temp.txt') is not True or os.path.getsize(r'C:\Users\Marty Mooney\Desktop\program_temp.txt') == 0:
    r'C:\Users\Marty Mooney\Desktop\program_temp.txt') == 0:
    temp_file = open(r'C:\Users\Marty Mooney\Desktop\program_temp.txt', 'w')
    else:
    temp_file = open(r'C:\Users\Marty Mooney\Desktop\program_temp.txt', 'a')

    for item in ip_regex_o_search:
        ping_output = subprocess.check_output(["ping",item]).decode()
    print(ping_output)
    temp_file.write(f'IP address is:\n{item}\n\nping output:\n{ping_output}\n\n')
