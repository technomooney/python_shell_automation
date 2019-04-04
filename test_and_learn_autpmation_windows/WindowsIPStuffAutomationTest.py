import os,re, subprocess, paramiko


def main():
if os.name == 'posix':
    print(os.name)
    ipconfig_var = subprocess.run(['ifconfig', '-a'], capture_output=True).stdout.decode()
elif os.name == 'nt':
    print(os.name)
    ipconfig_var = subprocess.run(["ipconfig", '/all'], capture_output=True).stdout.decode()
    print(ipconfig_var)

# print(str(ipconfig_var))

find_target_ip_regex_object =re.compile(r'IPv4 Address. . . . . . . . . . . : \d{1,3}[.]\d{1,3}[.]\d{1,3}[.]\d{1,3}')


ip_regex_o = re.compile(r'192{1,3}[.]\d{1,3}[.]\d{1,3}[.]\d{1,3}|10[.]\d{1,3}[.]\d{1,3}[.]\d{1,3}')
# print(type(ipconfig_var))
ip_regex_o_search = ip_regex_o.findall(ipconfig_var)
print(type(ipconfig_var))
print(ipconfig_var)
print(ip_regex_o_search)

if os.path.exists(r'.\program_temp.txt') is not True or os.path.getsize(r'.\program_temp.txt') == 0:
    temp_file = open(r'.\program_temp.txt', 'w')
else:
    temp_file = open(r'.\program_temp.txt', 'a')

for item in ip_regex_o_search:
    ping_output = subprocess.check_output(["ping",item]).decode()
    print(ping_output)
    temp_file.write(f'IP address is:\n{item}\n\nping output:\n{ping_output}\n\n')
